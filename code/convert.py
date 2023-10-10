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

def resizeAllJpg(path_to_folder='Data/', newhight=1080, newwid=1080):
  jpgs = glob.glob(path_to_folder + '*.jpg')
  for image in jpgs:
      name_without_extension = os.path.splitext(image)[0]
      img = cv2.imread(image)
      resized, newheight, newwidth = resizeTo(img, newhight, newwid)
      cv2.imwrite(name_without_extension + ".jpg", resized)


def convertVideoToImage(path_to_folder='Video/', frame_rate=1):
    for fi in os.listdir(path_to_folder):
        nam, ext = os.path.splitext(fi)
        if fi.endswith('.mp4') or fi.endswith('.MP4'):
            out = path_to_folder + '/' + nam
            print(out)
            cam = cv2.VideoCapture(path_to_folder + fi)
            all_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) 
            try:
                if not os.path.exists(out):
                    os.makedirs(out)
            except OSError:
                pass
            currentframe = 0
            with tqdm.tqdm(total=all_frames) as pbar:
                pbar.set_description('Converting video: ' + fi)
                while(True):
                    ret,frame = cam.read()
                    if ret:
                        name = out + nam + '' + 'frame_' + str(currentframe) + '.jpg'
                        if currentframe % frame_rate == 0:
                            print('Saving frame: ' + name)
                            cv2.imwrite(name, frame)
                        # cv2.imwrite(name, frame)
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

def convert2Gray(path_to_folder='Dataset/'):
    jpgs = glob.glob(path_to_folder  + '*.jpg')
    for jpg in jpgs:
        flute = cv2.imread(jpg, 0)
        cv2.imwrite(jpg, flute)

def check_for_img(path_to_folder):
    for image in os.listdir(path_to_folder):
        if image.endswith(".jpg"):
            pass
        elif os.path.isdir(path_to_folder + image) == True:
            pass
        else:
            convertVideoToImage(path_to_folder, path_to_folder)
            os.remove(path_to_folder + image)
