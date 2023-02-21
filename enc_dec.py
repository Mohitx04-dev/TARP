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
from rev_slicing_transposition import rev_slicing
try:
    import numpy as np
    from PIL import Image
    from PIL import UnidentifiedImageError

except ModuleNotFoundError:
    print('Enter the command: pip install pillow numpy')
    sys.exit()

class ImageEncryption():
    def __init__(self, password):
        self.password = password
    def encrypt(self, filename):
        start = datetime.now()
        im =Image.open(filename).convert('RGB')
        colors = self.get_pixels(im)
        numbers = self.password_to_numbers(self.password)
        encrypted = colors
        for i in progress_bar(numbers, 'Encryption: '):
            encrypted = self.rail_fence_encrypt(encrypted, i)
        new_filename_e = new_filename('e')
        self.create_and_save_image(encrypted, im.width, im.height, new_filename_e, 'e')
        # print('Time:', datetime.now() - start)

    def decrypt(self, filename):
        start = datetime.now()
        im = Image.open(filename)
        colors = self.get_pixels(im)
        numbers = self.password_to_numbers(self.password[::-1])
        decrypted = colors
        for i in progress_bar(numbers, 'Decryption: '):
            decrypted = self.rail_fence_decrypt(decrypted, i)
        new_file = new_filename('d', filename)
        if new_filename:
            self.create_and_save_image(decrypted, im.width, im.height, new_file, 'd')
            rev_slicing(new_file)
            # print('Time:', datetime.now() - start)
        else:
            print('Error: the path is already taken')

    @staticmethod
    def get_pixels(im):
        colors = []
        for x in progress_bar(range(im.width), 'Scanning: '):
            for y in range(im.height):
                color = im.getpixel((x, y))
                colors.append(color)
        return colors

    @staticmethod
    def password_to_numbers(password):
        numbers = [ord(i) for i in password]
        return numbers

    def rail_fence_encrypt(self, plaintext, rails):
        p = self.rail_pattern(rails)
        return sorted(plaintext, key=lambda i: next(p))

    def rail_fence_decrypt(self, ciphertext, rails):
        p = self.rail_pattern(rails)
        indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
        result = [''] * len(ciphertext)
        for i, c in zip(indexes, ciphertext):
            result[i] = c
        return result

    @staticmethod
    def rail_pattern(n):
        r = list(range(n))
        return cycle(r + r[-2:0:-1])

    @staticmethod
    def create_and_save_image(colors, width, height, filename, mode):
        im = Image.new('RGB', (width, height))
        image_array = np.array(im)
        i = 0
        for x in progress_bar(range(width), 'Creation: '):
            for y in range(height):
                r = colors[i][0]
                g = colors[i][1]
                b = colors[i][2]
                image_array[y][x] = (r, g, b)
                i += 1
        new_image = Image.fromarray(image_array, 'RGB')
        new_image.save(filename)
        if mode == 'e':
            print(f'Encrypted image saved as {filename}')
        # elif mode == 'd':
        #     print(f'Decrypted image saved as {filename}')


def progress_bar(it, prefix='', size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size*j/count)
        # print(f"{prefix}[{u'='*x}{('·'*(size-x))}] {j}/{count}", end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    # print('\n', flush=True, file=out)


def runner(filename,mode,password):
    try:
        Image.open(filename)
    except (FileNotFoundError, UnidentifiedImageError) as error:
        print(error)
        return
    if len(password) > 0:
        if mode == 'd' or mode == 'D':
            ImageEncryption(password).decrypt(filename)
        else:
            ImageEncryption(password).encrypt(filename)
    else:
        print('Error: empty password')
        return
