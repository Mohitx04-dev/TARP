from text_to_image import tti
import getpass
from enc_dec import runner
def fun(password,mode,data):
    # password = getpass.getpass(prompt='Enter password: ', stream=None)
    # mode = input('Enter e or d \n')
    if(mode=='e'):
        return tti(password,data)
    else:
        filename = './Images/'+data
        return runner(filename,'d',password)