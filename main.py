#! /bin/python
import os, sys
import time
import inquirer
from code.convert import *
from code.helper.utils import *
from code.helper.imageTools import *
from code.helper.utils import *
from code.helper.fancy import *
from code.helper.threading import *
from code.helper.exif_data import *

path = '/media'

def end_program():
    a = input('Do you have something else to do? (y/n)')
    if a == 'y':
        main()
    elif a == 'n':
        print('Exiting')
        banner_goodbye()
        clear()
        exit()

def main():
    display_banner()
    selection_program()
    os_check()
    time.sleep(5)
    clear()
    question = [inquirer.List('selection',
                           message=" Main machine interface, what do you wish to do?",
                           choices=['Convert multimedia data to JPEG images', 'Beta test a function', 'Exit'],
                       ),]
    answer = inquirer.prompt(question)
    print(answer['selection'])
    a = answer['selection']
    if a == 'Convert multimedia data to JPEG images':
        clear()
        data_processing_banner()
        print('Converting multimedia data to JPEG images')
        path = check_full_path(path)
        temp = input('Use temporary folder folder? (y/n)')
        for file in os.listdir(path):
                if file.endswith('.mp4') or file.endswith('.MP4'):
                    print('Converting video to image series (saved to subfolder)')
                    convertVideoToImage(path)
                    print('Video converted')
                    Exif_origin = choose_meta(path)
                    print('Copying metadata')
                    end_program()
                elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.tiff') or file.endswith('.bmp'):
                        convert(path, False)
                        print('Images converted')
                        end_program()
                else:
                    print('File type not supported')
    elif a == 'Beta test a function':
        clear()
        beta_banner()
        error_banner()
        print(bcolors.ERROR + 'Function not yet implemented')
        reset_color()
    elif a == 'Exit':
        clear()
        end_program()
    else:
        print('Invalid selection')
        time.sleep(2)
        main()


if __name__ == '__main__':
    os.system('export TERM=xterm-256color')
    main()

