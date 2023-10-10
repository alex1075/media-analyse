import cv2
import os
import subprocess
import inquirer
import platform
from PIL import Image

def os_check():
    # for windows
    if platform.system() == 'Windows':
        print('Windows OS detected.')
        print('WARNING! Some functions may not work properly on your OS')
    # for mac and linux(here, os.name is 'posix')
    else:
        print('POSIX system detected.')

def choose_meta(path):
    array = []
    for d in os.listdir(path):
        if d.endswith('.ARW') == True or d.endswith('.jpg') or d.endswith('.JPG') or d.endswith('.png') or d.endswith('.PNG') or d.endswith('.tiff') or d.endswith('.TIFF') or d.endswith('.bmp') or d.endswith('.BMP'):
            array.append(path + d)
    question = [inquirer.List('image',
                            message="Which image do you want to copy the exif data from?",
                            choices=array,
                        ),]
    answer = inquirer.prompt(question)
    return answer['image']   

def choose_framerate():
    array = [16, 24, 25, 30, 48, 50, 60, 120, 'Non standard']
    question = [inquirer.List('FPS',
                            message="What is the framerate of the recording device?",
                            choices=array,
                        ),]
    answer = inquirer.prompt(question)
    if answer['FPS'] == 'Non standard':
        question = [inquirer.Text('FPS',
                            message="What is the framerate of the recording device?",
                        ),]
        answer = inquirer.prompt(question)
        return answer['FPS']
    else:    
        return answer['FPS']
