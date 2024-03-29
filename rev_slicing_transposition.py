from PIL import Image
from image_to_text import image_to_text
def rev_slicing(filename):
# Opens a image in RGB mode
    im = Image.open(filename)

    width, height = im.size
    
    # Setting the points for cropped image
    l1 = 0
    t1 = 0
    r1 = width/4
    b1 =   height /2
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((l1, t1, r1, b1))

    # Setting the points for cropped image
    l2 = width/4
    t2 = 0
    r2 = width/2
    b2 =   height /2
    
    # Cropped image of above dimension
    # (It will not change original image)
    im2 = im.crop((l2, t2, r2, b2))

    # Setting the points for cropped image
    l3 = width/2
    t3 = 0
    r3 = 3* (width/4)
    b3 =   height /2
    
    # Cropped image of above dimension
    # (It will not change original image)
    im3 = im.crop((l3, t3, r3, b3))

    # Setting the points for cropped image
    l4 = 3* width/4
    t4 = 0
    r4 = width
    b4 =   height /2
    
    # Cropped image of above dimension
    # (It will not change original image)
    im4 = im.crop((l4, t4, r4, b4))
    
    # fim=im1+im2+im3+im4
    #Shows the image in image viewer
    Image.blend(Image.blend(im1,im2,0.5),Image.blend(im3,im4,0.5),0.5).save(filename)
    return image_to_text(filename)
