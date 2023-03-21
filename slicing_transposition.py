# 8 bit slicing
import numpy as np
import cv2
from PIL import Image
import getpass
import os
import random
import sys
from datetime import datetime
from itertools import cycle
from filename_generator import new_filename
from enc_dec import runner
try:
    import numpy as np
    from PIL import Image
    from PIL import UnidentifiedImageError
except ModuleNotFoundError:
    print('Enter the command: pip install pillow numpy')
    sys.exit()

def transpose(filename,password):
    # Read the image in greyscale
    img = cv2.imread(filename,0)
    
    #Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
    lst = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lst.append(np.binary_repr(img[i][j] ,width=8)) # width = no. of bits


    # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
    # Multiply with 2^(n-1) and reshape to reconstruct the bit image.
    eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])

    seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
    six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
    five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
    four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])

    three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
    two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
    one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])
    
    #Concatenate these images for ease of display using cv2.hconcat()
    finalr = cv2.hconcat([eight_bit_img,seven_bit_img,six_bit_img,five_bit_img])
    finalv =cv2.hconcat([four_bit_img,three_bit_img,two_bit_img,one_bit_img])
    
    # Vertically concatenate
    final = cv2.vconcat([finalr,finalv])

    # transposition of sliced image
    fi=cv2.transpose(final)

    cv2.waitKey(0)
    t_filename = new_filename('t')
    cv2.imwrite(t_filename, final)
    return runner(t_filename,'e',password)