import os
from random import *

def shuffle():
    file_list = os.listdir(r"/home/tiffany/Downloads/secret message")
    print(file_list)
    path = os.getcwd()
    os.chdir("/home/tiffany/Downloads/secret message")
    print(path)
    for file_name in file_list:
        random = randint(1, 1000)
        os.rename(file_name, str(random) + file_name)
        print(file_name)



def decipher():
    file_list = os.listdir(r"/home/tiffany/Downloads/secret message")
    print(file_list)
    path = os.getcwd()
    os.chdir("/home/tiffany/Downloads/secret message")
    print(path)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '1234567890'))
        print(file_name)


decipher()
# shuffle()
