import os
import cv2
import numpy as np
import csv
import time
import sys
import glob
from openpose import *
from yoga.images import *
from yoga.joints import *
from yoga.instruction import *
from yoga.openpose_parameter import *
from yoga.yoga_pose_joint_parameters import *
from yoga.output import *
print('-----packages loaded-----')


def frame_with_angle_minimal_version(frame):
    #Load parameters for openpose
    params = get_parameters(net_resolution='-1x368', model_pose='BODY_25')
    openpose = OpenPose(params)
    main_joints, keypoints_dictionary =  get_main_joint_parameters_BODY25()
    #create output dir if it does not exist
    if not os.path.exists('output/pics'):
        os.makedirs('output/pics')
        print('created directory')
    original = 'output/pics/original_' + str(time.time()) + '.png'
    cv2.imwrite(original, frame)
    keypoints, output_image = openpose.forward(frame, True)
    # output image with keypoints
    pic_name = 'output/pics/keypoints' + str(time.time()) + '.png'
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
    pic_name = 'output/pics/angles' + str(time.time()) + '.png'
    cv2.imwrite(pic_name, output_image)
    return real_angles

def write_csv_file_with_angles_for_pose(pics_directory, file_name_csv):
    #built paths of all images in folder
    paths = os.path.join(pics_directory, '*.jpg')
    print(paths)
    pose_paths = glob.glob(paths)
    print('-----file paths images collected-----', pose_paths)
    all_images = load_images('', pose_paths)
    print('--images loaded----')
    #Write HEADER
    header = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
    #file_name_csv = 'warrior2left_iyengar.csv'
    write_to_csv(file_name_csv, header)
    #GET ANGLES AND WRITE TO CSV FILE
    for counter in all_images:
        data = frame_with_angle_minimal_version(all_images[counter])
        write_to_csv(file_name_csv, data)
        print('Currently processing frame', counter, 'out of', len(all_images))

#write_csv_file_with_angles_for_pose('../get_frames/youtube_data/Jessamyn/Jessamy_transitions/', 'jessy_transition.csv')
write_csv_file_with_angles_for_pose('../get_frames/youtube_data/Jessamyn/Jessamy_w2_left', 'jessy_w2_left.csv')

