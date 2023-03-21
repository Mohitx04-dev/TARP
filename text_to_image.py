from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from filename_generator import new_filename
from slicing_transposition import transpose
def tti(password, plaintext):
    img = Image.new('RGB', (200, 200), color = (255,255,255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("./templates/NotoSans-Regular.ttf", size=20)
    d.text((40,30), plaintext, fill=(0,0,0),font=font)
    filename = new_filename('i')
    img.save(filename)
    #--------------------------------------------#
    return transpose(filename,password)
