import cv2
import glob, os
from PIL import Image
from code.helper.utils import *
from code.helper.imageTools import *
import shutil
import tqdm


def convert(path_to_folder='Data/', save_to_new=False, save_path='temp/'):
    for infile in tqdm.tqdm(os.listdir(path_to_folder), desc='Converting images', unit='images'):
        if infile[-3:] == "bmp":
            outfile = infile[:-3] + "jpg"
            im = Image.open(path_to_folder + infile)
            out = im.convert("RGB")
            if save_to_new == True:
                out.save(save_path + outfile, "jpeg", quality=100)
            else:
                out.save(path_to_folder + outfile, "jpeg", quality=100)
            os.remove(path_to_folder + infile)
        elif infile[-4:] == "tiff":
            outfile = infile[:-4] + "jpg"
            im = Image.open(path_to_folder + infile)
            out = im.convert("RGB")
            if save_to_new == True:
                out.save(save_path + outfile, "jpeg", quality=100)
            else:
                out.save(path_to_folder + outfile, "jpeg", quality=100)
            os.remove(path_to_folder + infile)
        elif infile[-3:] == "png":
            outfile = infile[:-3] + "jpg"
            img = cv2.imread(path_to_folder + infile)
            if save_to_new == True:
                cv2.imwrite(save_path + outfile, img)
            else:
                cv2.imwrite(path_to_folder + outfile, img)
            os.remove(path_to_folder + infile)
        elif infile[-3:] == "jpg" or infile[-3:] == "jpeg":
            try:
                shutil.copy(path_to_folder + infile, save_path + infile)
                os.remove(path_to_folder + infile)
            except:
                pass
        else:
            pass

def resizeAllJpg(path_to_folder='Data/', newhight=1080, newwid=1080):
  jpgs = glob.glob(path_to_folder + '*.jpg')
  for image in jpgs:
      name_without_extension = os.path.splitext(image)[0]
      img = cv2.imread(image)
      resized, newheight, newwidth = resizeTo(img, newhight, newwid)
      cv2.imwrite(name_without_extension + ".jpg", resized)


def convertVideoToImage(path_to_folder='Video/'):
    for fi in os.listdir(path_to_folder):
        nam, ext = os.path.splitext(fi)
        if fi.endswith('.mp4'):
            out = os.system('mkdir ' + path_to_folder + ' ' + nam)
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
                        name = out + nam + '/' + '_frame_' + str(currentframe) + '.jpg'
                        cv2.imwrite(name, frame)
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

def convertAVideoToImage(video):
            cam = cv2.VideoCapture(video)
            all_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) 
            currentframe = 0
            with tqdm.tqdm(total=all_frames) as pbar:
                pbar.set_description('Converting video: ' + video)
                while(True):
                    ret,frame = cam.read()
                    if ret:
                        ni = name.split('/')
                        name = video[:-4] + '/' + ni[-1] + '_frame_' + str(currentframe) + '.jpg'
                        # print(name)
                        cv2.imwrite(name, frame)
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
