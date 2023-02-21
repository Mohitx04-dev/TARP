from PIL import Image, ImageFilter, ImageEnhance
from pytesseract import pytesseract
# Defining paths to tesseract.exe
# and the image we would be using
def image_to_text(filename):
    path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"#Define path to image
    im = Image.open(filename)
    pytesseract.tesseract_cmd = path_to_tesseract
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(im, lang='eng',config='--psm 7')
    # Displaying the extracted text
    print(text[:-1])
    