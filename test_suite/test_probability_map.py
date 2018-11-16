import sys
sys.path.append('../')

from yoga.general_setup import *
from yoga.images import *
from yoga.probability_map import *


img_single = load_images('../sample_images/', ['side_planck.jpeg'])
img_single = img_single[0]
#todo add coco & mpi
prototxt = "../models/pose/body_25/pose_deploy.prototxt"
caffemodel = "../models/pose/body_25/pose_iter_584000.caffemodel"
number_of_keypoints = 25
in_size = (img_single.shape[0], img_single.shape[1])
output = probability_map(prototxt, caffemodel,img_single , in_size)
print(output)
#cv2.imwrite('test.png', img_single[0])



