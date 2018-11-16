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
    original = 'output/original_' + str(time.time()) + '.png'
    cv2.imwrite(original, frame)
    keypoints, output_image = openpose.forward(frame, True) 
    # output image with keypoints
    pic_name = 'output/keypoints' + str(time.time()) + '.png'
    cv2.imwrite(pic_name, output_image)
    real_angles = get_angles_between_ligaments(main_joints , keypoints_dictionary, keypoints, print_output=True) 
    count = -1
    #loop through the main_joint tripels of body, e.g. first triple with keypoints (2-3-4)
    for pairs in main_joints:
          count += 1
          #get the keypoint of middle joint (3)  
          middle_joint = pairs[1]
          #map each keypoint to corresponding matrix elements
          p2 = map_keypoint_index_to_coordinate(keypoints, middle_joint)
          #overlay calculated angles over image
          if np.isnan(real_angles[count]) == False:
            cv2.putText(output_image, "{}".format(int(np.round(real_angles[count]))), (int(p2[0]), int(p2[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, lineType=cv2.LINE_AA)
    pic_name = 'output/angles' + str(time.time()) + '.png'
    cv2.imwrite(pic_name, output_image)
    return real_angles




header = [["a1", "a2", "a3", "a4", "a5", "a6"]]
file_name_csv = 'output/transition_lets_try.csv'
write_to_csv(file_name_csv, header)

#img_collection =  load_images(, file_list)

for image in img_collection:
    angle_of_frame = frame_with_angle(image)
    write_to_csv(file_name_csv, angle_of_frame)

  
