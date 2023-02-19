
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (280, 60), color = (255,255,255))
 
d = ImageDraw.Draw(img)
d.text((10,20), "hello world we have been found save yourself", fill=(0,0,0))
 
img.save('tti.png')