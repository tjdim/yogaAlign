import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm
import math

def map_keypoint_index_to_coordinate(keybody_points,mm):
        x_index = mm * 3
        y_index = mm * 3 +1

        px = keybody_points.item(x_index)
        py = keybody_points.item(y_index)

        return np.array([px, py])


def get_angles_vectors(u,v):
        c = dot(u,v)/norm(u)/norm(v)
        alpha = np.degrees(arccos(clip(c, -1, 1)))
        return(alpha)

def get_angles_vectors_sign(u,v):
    dot = u[0]*v[0] + u[1]*v[1]
    det = u[0]*v[1] - u[1]*v[0]
    return math.atan2(det, dot)/math.pi*180.


def get_body_keypoints(frame, output, number_of_keypoints):
    frameCopy = np.copy(frame)
    #define parameters
    threshold = 0.1 
    out_size = (output.shape[3],output.shape[2]) 
    circ_size = 3
    points = []
    for i in range(0,number_of_keypoints):
        minVal, prob, minLoc, point = cv2.minMaxLoc(output[0, i, :, :])
        x = (frame.shape[1] * point[0]) / out_size[0]
        y = (frame.shape[0] * point[1]) / out_size[1]
        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), circ_size, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(x), int(y)), circ_size, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
            plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else :
            points.append(None)
    return points



def get_angles_between_ligaments(POINTS,points_dictionary,keybody_points, print_output=False):
    angles = []
    MAIN_JOINTS = [[2,3,4],[5,6,7],[12,13,14],[9,10,11],[10, 9, 2], [13,12,5], [9, 2 ,3], [12, 5, 6]]
    #PAIRS = [[2,3,4],[5,6,7],[12,13,14],[9,10,11],[10, 9, 2], [13,12,5], [9, 5 ,3], [12, 5, 6]]
    for pairs in MAIN_JOINTS:        
        mm = pairs[0]
        nn = pairs[1]
        oo = pairs[2]

        p1 = map_keypoint_index_to_coordinate(keybody_points,mm)
        p2 = map_keypoint_index_to_coordinate(keybody_points,nn)
        p3 = map_keypoint_index_to_coordinate(keybody_points,oo)

        u = p1-p2
        v = p3-p2
     
        alpha = get_angles_vectors(u,v)
        print(alpha)
        angles.append(alpha)
    return angles
