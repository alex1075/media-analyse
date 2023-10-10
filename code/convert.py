import cv2
import glob, os
from PIL import Image
from code.helper.utils import *
from code.helper.imageTools import *
import shutil
import tqdm


def convert(path_to_folder='Data/', save_path='jpegs/'):
    # save_path = check_full_path(save_path)
    for infile in tqdm.tqdm(os.listdir(path_to_folder), desc='Converting images', unit='images'):
        if infile[-3:] == "bmp" or infile[-3:] == "BMP" or infile[-3:] == "tif" or infile[-3:] == "TIF" or infile[-3:] == "raw" or infile[-3:] == "RAW" or infile[-3:] == "dng" or infile[-3:] == "DNG" or infile[-4:] == "tiff" or infile[-4:] == "TIFF" or infile[-3:] == 'ARW' or infile[-3:] == 'arw':
            outfile = infile[:-3] + "jpg"
            os.system('iconvert' + ' ' + str(path_to_folder) + str(infile) + ' ' + str(save_path) + str(outfile))
            os.remove(path_to_folder + infile)
        elif infile[-3:] == "jpg" or infile[-3:] == "jpeg":
            shutil.copy(str(path_to_folder) + str(infile), str(save_path) + str(infile))
            os.remove(path_to_folder + infile)
        else:
            pass

def convertAVideoToImage(video, path, frame_rate=1):
            try:
                os.system('mkdir ' + path + '/' +video[:-4])
            except:
                pass
            cam = cv2.VideoCapture(path + video)
            all_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) 
            currentframe = 0
            with tqdm.tqdm(total=all_frames) as pbar:
                pbar.set_description('Converting video: ' + video)
                while(True):
                    ret,frame = cam.read()
                    if ret:
                        ni = video.split('/')
                        out = video[:-4] + '/' + 'frame_' + str(currentframe) + '.jpg'
                        if currentframe % int(frame_rate) == 0:
                            cv2.imwrite(path + out, frame)
                        currentframe += 1
                        pbar.update(1)
                    else:
                        break
            pbar.close()        
            cam.release()
            try:
                cv2.destroyAllWindows()
            except:
                pass
            return path + '/' + video[:-4] + '/'