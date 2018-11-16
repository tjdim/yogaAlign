from os.path import join
import cv2
import matplotlib.pyplot as plt


def load_images(img_dir, file_list):
    '''Built paths from dir name and list of file names
    
       Returns:
           img_dict (dict): contains np.array of all images
    '''
    img_path = [join(img_dir, filename) for filename in file_list]
    img_dict = {}
    for jj in range(0, len(img_path)):
        img_dict[jj] = cv2.imread(img_path[jj])
        #img_dict[jj] = cv2.resize(img_dict[jj], (368, 368))
    return img_dict

def load_images_from_path(img_path):
    '''
       Returns:
           img_dict (dict): contains np.array of all images
    '''
    img_dict = {}
    for jj in range(0, len(img_path)):
        img_dict[jj] = cv2.imread(img_path[jj])
        img_dict[jj] = cv2.resize(img_dict[jj], (368, 368))

    return img_dict

def display_images(img_collection, display_all=False, subplt = True):
    '''
    img_collection (dict) : keys: pic_identifier (int)
                            values: pic as np.array
    display_number (boolean): specifies number of pics to display
                              False (default) displays only first image
                              True display all images in collection
    '''
    # convert color space of image from BGR to RGB
    color_space_flag = cv2.COLOR_BGR2RGB
    # default image size
    
    
    if(display_all==True):
        if (type(img_collection)==list):
            number_of_pics = len(img_collection)
        else:
            number_of_pics = len(img_collection.keys())
    else:
        number_of_pics = 1
    imgsize_default = [20,200]
    
    if(subplt==False):
        mod = number_of_pics%2
        if(mod==0):
            col_num = 2
            row_num = number_of_pics/2
        elif(mod==1 and number_of_pics==1):
            col_num = 1
            row_num = 1
        elif(mod==1 and number_of_pics>2):
            col_num = 3
            row_num = number_of_pics/3
    else:
            col_num = 1
            row_num = number_of_pics
     
       
    fig = plt.figure(figsize = imgsize_default)
    for jj in range(1, number_of_pics+1):
        tmp = cv2.cvtColor(img_collection[jj-1], color_space_flag)
        fig.add_subplot(row_num, col_num, jj)
        plt.imshow(tmp)
