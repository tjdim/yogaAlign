import sys
sys.path.append('../')
from yoga.general_setup import *
from yoga.images import *
from yoga.yogaAlignAngle import *


img_single = load_images('../sample_images/', ['side_planck.jpeg'])
img_single = img_single[0]

frame_with_angle(img_single)

frame_with_angle(img_single)

