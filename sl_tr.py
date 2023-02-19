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
try:
    import numpy as np
    from PIL import Image
    from PIL import UnidentifiedImageError
except ModuleNotFoundError:
    print('Enter the command: pip install pillow numpy')
    sys.exit()

# Read the image in greyscale
img = cv2.imread('tti.png',0)
 
#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
print(img.shape[0], img.shape[1])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        #  print(img[i][j])
        #  print(img[i][j])
        #  print(i, j)
        #  print('adfdjkf')
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

cv2.imshow('Sliced Image',fi)
cv2.waitKey(0)
cv2.imwrite("sliced.png", final)
# # Display the images
# cv2.imshow('Final Image',fi)
# cv2.waitKey(0) 

# slicing over, image final

# --------

#-------------------------------------

# #Encryption of sliced and transposed image

# class ImageEncryption():
#     def __init__(self, password):
#         self.password = password

#     def encrypt(self, filename):
#         start = datetime.now()
#         im =Image.open(filename).convert('RGB')
#         colors = self.get_pixels(im)
#         numbers = self.password_to_numbers(self.password)
#         encrypted = colors
#         for i in progress_bar(numbers, 'Encryption: '):
#             encrypted = self.rail_fence_encrypt(encrypted, i)
#         new_filename = self.new_filename('e')
#         self.create_and_save_image(encrypted, im.width, im.height, new_filename, 'e')
#         print('Time:', datetime.now() - start)

#     def decrypt(self, filename):
#         start = datetime.now()
#         im = Image.open(filename)
#         colors = self.get_pixels(im)
#         numbers = self.password_to_numbers(self.password[::-1])
#         decrypted = colors
#         for i in progress_bar(numbers, 'Decryption: '):
#             decrypted = self.rail_fence_decrypt(decrypted, i)
#         new_filename = self.new_filename('d', filename)
#         if new_filename:
#             self.create_and_save_image(decrypted, im.width, im.height, new_filename, 'd')
#             print('Time:', datetime.now() - start)
#         else:
#             print('Error: the path is already taken')

#     @staticmethod
#     def get_pixels(im):
#         print('')
#         colors = []
#         for x in progress_bar(range(im.width), 'Scanning: '):
#             for y in range(im.height):
#                 color = im.getpixel((x, y))
#                 colors.append(color)
#         return colors

#     @staticmethod
#     def password_to_numbers(password):
#         numbers = [ord(i) for i in password]
#         return numbers

#     def rail_fence_encrypt(self, plaintext, rails):
#         p = self.rail_pattern(rails)
#         return sorted(plaintext, key=lambda i: next(p))

#     def rail_fence_decrypt(self, ciphertext, rails):
#         p = self.rail_pattern(rails)
#         indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
#         result = [''] * len(ciphertext)
#         for i, c in zip(indexes, ciphertext):
#             result[i] = c
#         return result

#     @staticmethod
#     def rail_pattern(n):
#         r = list(range(n))
#         return cycle(r + r[-2:0:-1])

#     @staticmethod
#     def new_filename(mode, filename=None):
#         while True:
#             if filename is None:
#                 while True:
#                     number = ''.join([str(random.randint(0, 9)) for _ in range(5)])
#                     new_filename = f'{mode}i-{number}.png'
#                     if os.path.exists(new_filename):
#                         continue
#                     else:
#                         break
#                 return new_filename
#             else:
#                 number = filename.split('i-')[1].split('.')[0]
#                 new_filename = f'{mode}i-{number}.png'
#                 if os.path.exists(new_filename):
#                     return None
#                 else:
#                     return new_filename

#     @staticmethod
#     def create_and_save_image(colors, width, height, filename, mode):
#         im = Image.new('RGB', (width, height))
#         image_array = np.array(im)
#         i = 0
#         for x in progress_bar(range(width), 'Creation: '):
#             for y in range(height):
#                 r = colors[i][0]
#                 g = colors[i][1]
#                 b = colors[i][2]
#                 image_array[y][x] = (r, g, b)
#                 i += 1
#         new_image = Image.fromarray(image_array, 'RGB')
#         new_image.save(filename)
#         if mode == 'e':
#             print(f'Encrypted image saved as {filename}')
#         elif mode == 'd':
#             print(f'Decrypted image saved as {filename}')


# def progress_bar(it, prefix='', size=60, out=sys.stdout):
#     count = len(it)

#     def show(j):
#         x = int(size*j/count)
#         print(f"{prefix}[{u'='*x}{('·'*(size-x))}] {j}/{count}", end='\r', file=out, flush=True)
#     show(0)
#     for i, item in enumerate(it):
#         yield item
#         show(i+1)
#     print('\n', flush=True, file=out)


# def main():
#     filename = input('Enter image filename: ')
#     try:
#         Image.open(filename)
#     except (FileNotFoundError, UnidentifiedImageError) as error:
#         print(error)
#         return
#     password = getpass.getpass(prompt='Enter password: ', stream=None)
#     if len(password) > 0:
#         mode = input('Do you want to encrypt or decrypt the image [E/d]? ')
#         if mode == 'd' or mode == 'D':
#             ImageEncryption(password).decrypt(filename)
#         else:
#             ImageEncryption(password).encrypt(filename)
#     else:
#         print('Error: empty password')
#         return


# if __name__ == '__main__':
#     main()

