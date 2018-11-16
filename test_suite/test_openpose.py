import sys
sys.path.append('../')
from yoga.general_setup import *
from yoga.images import *
from openpose import *
from yoga.openpose_parameter import *
import time
import csv

def test_openpose(test_image, resolution='-1x368' , pose="BODY_25"):
  params = get_parameters(net_resolution=resolution, model_pose=pose)
  print(params)
  openpose = OpenPose(params)

  keypoints, output_image = openpose.forward(test_image, True)
  cv2.imwrite(f'png/test_openpose_{pose}_{resolution}.png', output_image)
  return

default_timer = time.time

models = ['BODY_25', 'COCO', 'MPI']
timing = []
img_single = load_images('../sample_images/',  ['side_planck_high_res.jpeg', 'side_planck.jpeg'])
img_single = img_single[0]

for string in models:
  for jj in range(1, 10, 5):
    start = default_timer()
    test_openpose(test_image = img_single, resolution = f"-1x{jj*16}", pose = string)
    finish = default_timer()
    timing.append([finish-start, string, jj*16])
  

for ii in range(0,len(timing)):
  print(f'Your model {timing[ii][1]} needs {timing[ii][0]} seconds with res of {timing[ii][2]}')

myFile = open('timing_models_resolution.csv', 'w')
header = [[ "time (sec)", "model","resolution"]]
with myFile:
        writer = csv.writer(myFile)
        writer.writerows(header)
        writer.writerows(timing)

