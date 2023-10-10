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

def main():
    path = 'test_folder/' # debug only
    # path = '/media' # production
    # display_banner()
    # selection_program()
    # os_check()
    # time.sleep(5)
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
        # data_processing_banner()
        print('Converting multimedia data to JPEG images')
        fps = choose_framerate()
        path = check_full_path(path)
        for file in os.listdir(path):
                # print(file)
                if file.endswith('.mp4') or file.endswith('.MP4'):
                    # print(file)
                    print('Converting video to image series (saved to subfolder)')
                    convertAVideoToImage(file, path, fps)
                    print('Video converted')
                    Exif_origin = choose_meta(path)
                    print('Copying metadata')
                    # end_program()
                elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.tiff') or file.endswith('.bmp'):
                        convert(path, False)
                        print('Images converted')
                        # end_program()
                elif file.endswith('.ARW') or file.endswith('.arw'):
                     pass
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

