from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from filename_generator import new_filename
from slicing_transposition import transpose
def tti(password, plaintext):
    img = Image.new('RGB', (200, 200), color = (255,255,255))
    d = ImageDraw.Draw(img)
    d.text((10,20), plaintext, fill=(0,0,0))
    filename = new_filename('i')
    img.save(filename)
    #--------------------------------------------#
    transpose(filename,password)
