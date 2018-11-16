import os
import cv2
import numpy as np
import csv
import time
import sys
from openpose import *
from yoga.joints import *
from yoga.instruction import *
from yoga.openpose_parameter import *
from yoga.yoga_pose_joint_parameters import *
from yoga.output import *

def frame_with_angle(frame):
  params = get_parameters(net_resolution='-1x368', model_pose='BODY_25')
  openpose = OpenPose(params)
  main_joints, keypoints_dictionary =  get_main_joint_parameters_BODY25()  
  #hard coded solution for ref angle left  knee in front warrior 2
  REFANGLE_WARRIOR = [180,  180, 90,  180, 160, 90] 
  threshold = 10
  
  #write original image to file
  original = 'output/original_' + str(time.time()) + '.png'
  cv2.imwrite(original, frame)
  # get keypoints and output_image -> call openpose
  keypoints, output_image = openpose.forward(frame, True) 
  # output image with keypoints
  pic_name = 'output/keypoints' + str(time.time()) + '.png'
  cv2.imwrite(pic_name, output_image)
  print('----------frame with angle: output_image with keypoints printed----------------------')

  while(keypoints.size < 20):
        print('Where are you? Get into position')
        print('--------------------------------')
        instruction('a', 6, audio=True)
        if(keypoints.size<20):
            print('Yogaalign can not detect you. Check your camera')
            instruction('a', 7, audio=True)
            return
            #sys.exit("Detection Error")
  real_angles = get_angles_between_ligaments(main_joints , keypoints_dictionary, keypoints, print_output=True) 
  count = -1
  #loop through the main_joint tripels of body, e.g. first triple with keypoints (2-3-4)
  for pairs in main_joints:
        delta_alpha = 0 
        count += 1
        #get the keypoint of middle joint (3)  
        middle_joint = pairs[1]
        #map each keypoint to corresponding matrix elements
        p2 = map_keypoint_index_to_coordinate(keypoints, middle_joint)
        #overlay calculated angles over image
        if np.isnan(real_angles[count]) == False:
          cv2.putText(output_image, "{}".format(int(np.round(real_angles[count]))), (int(p2[0]), int(p2[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, lineType=cv2.LINE_AA)
          #for each frame we need to correct all angles
          ref_angle = REFANGLE_WARRIOR[count]
          real_angle = real_angles[count]
          delta_alpha = delta_alpha + abs(ref_angle -real_angle)
          print('--------------------------------------------')
          print('delta_alpha is ',delta_alpha)
          print('--------------------------------------------')
          instruct_case = get_diff_angles(ref_angle, real_angle) 
          body_part_to_move = keypoints_dictionary[middle_joint]
          instruction(body_part_to_move, instruct_case, audio=True)


  pic_name = 'output/angles' + str(time.time()) + '.png'
  cv2.imwrite(pic_name, output_image)


#  header = [["a1", "a2", "a3", "a4", "a5", "a6"]]
  file_name_csv = 'output/transition.csv'
  print(type(real_angles))
  write_to_csv(file_name_csv, real_angles)


  print("Writing complete")
  return output_image
