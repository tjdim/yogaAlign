sys.path.append('../')
from yoga.general_setup import *
from yoga.images import *


img_single = load_images('../sample_images/', ['side_planck.jpeg'])
print(type(img_single))

cv2.imwrite('test.png', img_single[0])

display_images(img_single)
