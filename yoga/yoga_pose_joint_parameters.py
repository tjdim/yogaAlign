def get_main_joint_parameters_BODY25():
    
    #MAIN_JOINTS = [[2,3,4],[5,6,7],[12,13,14],[9,10,11],[10, 9, 2], [13,12,5]]
    MAIN_JOINTS = [[2,3,4],[5,6,7],[12,13,14],[9,10,11],[10, 9, 2], [13,12,5], [9, 2 ,3], [12, 5, 6]]

    KEYPOINT_DICTIONARY =  {0:  "Nose", 1:  "Neck", 2:  "right Shoulder", 3:  "right Elbow", 4:  "right Wrist", 5:  "Left Shoulder", 6:  "Left Elbow", 7:  "Left Wrist", 8:  "MidHip", 9:  "Right Hip", 10: "Right Knee", 11: "Right Ankle", 12: "Left Hip", 13: "Left Knee", 14: "Left Ankle",
 15: "REye", 16: "LEye", 17: "REar", 18: "LEar", 19: "LBigToe", 20: "LSmallToe", 21: "LHeel", 22: "RBigToe", 23: "RSmallToe", 24: "RHeel", 25: "Background"}
    #pose fully determined by all angles (degrees of freedom)
    #define vectors of angle pairs between the following keypoints
    #0:  "RShoulder - RElbow - RWrist",
    #1:  "LShoulder - LElbow - LWrist",
    #2:  "LHip - LKnee - LAnkle",
    #3:  "RHip - RKnee - RAnkle",
    #4:  "RKnee - RHip - RShoulder",
    #5:  "LKnee - LHip - LShoulder",
    return MAIN_JOINTS, KEYPOINT_DICTIONARY 

