import cv2
import os
import subprocess
import inquirer
import platform
from PIL import Image

host_file = os.getcwd() + '/code/data/hosts'

def os_check():
    # for windows
    if platform.system() == 'Windows':
        print('Windows OS detected.')
        print('WARNING! Some functions may not work properly on your OS')
    # for mac and linux(here, os.name is 'posix')
    else:
        print('POSIX system detected.')

def check_full_path(path):
    if os.path.isabs(path) == True:
        return path
    else:
        if os.path.isabs(os.getcwd() + '/' + path) == True:
            return os.getcwd() + '/' + path
        else:
            raise Exception('Path not found')

#Grabs biggest dimension and scales the photo so that max dim is now 1280
def resizeTo(image, newhigh=1280, newwid=1280, inter=cv2.INTER_AREA):
    (height, width) = image.shape[:2]
    if height>width:
        newheight = newhigh
        heightratio = height/newheight
        newwidth = int(width/heightratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    elif width>height:
        newwidth = newwid
        widthratio = width/newwidth
        newheight = int(height/widthratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    else: 
        pass

def cat_file(file):
    os.system('cat ' + file)

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir)) + '/'

def choose_meta(path):
    array = []
    path = check_full_path(path)
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
    array = [24, 25, 30, 60, 120, 'Non standard']
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
