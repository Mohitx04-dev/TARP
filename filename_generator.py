import random
import os
def new_filename(mode, filename=None):
    while True:
        number = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        new_filename = f'./Images/{mode}-{number}.png'
        if os.path.exists(new_filename):
            continue
        else:
            break
    return new_filename