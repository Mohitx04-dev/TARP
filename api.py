from text_to_image import tti
import getpass
from enc_dec import runner
password = getpass.getpass(prompt='Enter password: ', stream=None)
mode = input('Enter e or d \n')
if(mode=='e'):
    pt = input("Enter Plain Text: \n")
    tti(password,pt)
else:
    filename = './Images/'+input('Enter encrypted filename \n')
    runner(filename,'d',password)