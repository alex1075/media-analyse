import os
import cv2
import tqdm
import numpy as np
from code.helper.utils import *


# Sharpen image using an unsharp mask
def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def imgSizeCheck(image, path, x, y):
    img = cv2.imread(path + image)
    height, width, channels = img.shape
    if height << y:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    elif width << x:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        cv2.imshow(corrected_img)
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    else:
        pass

# crop images in chunks of size (x,y) and adapt annotations
def crop_images(x, y, path, save_path):
    path = check_full_path(path)
    images = os.listdir(path)
    for image in tqdm.tqdm(images, desc="Cropping images"):
        if image.endswith(".jpg"):
            # print('Tick')
            img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                for j in range(0, width, x):
                    crop_img = img[i:i+y, j:j+x]
                    new_name = image[:-4] + '_' + str(i) + '_' + str(j)
                    cv2.imwrite(save_path + new_name + ".jpg", crop_img)
                img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                 for j in range(0, width, x):
                    crop = img[i:i+y, j:j+x]
                    cv2.imwrite(save_path + image[:-4] + '_' + str(i) + '_' + str(j) + '.jpg', crop)
            try:
                os.remove(save_path + image)
            except:
                pass
        else:
            pass

def crop_image_list(x, y, lists, path, save_path):
    images = lists
    for image in tqdm.tqdm(images, desc="Cropping images"):
            img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                for j in range(0, width, x):
                    crop_img = img[i:i+y, j:j+x]
                    new_name = image[:-4] + '_' + str(i) + '_' + str(j)
                    cv2.imwrite(save_path + new_name + ".jpg", crop_img)
                img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                 for j in range(0, width, x):
                    crop = img[i:i+y, j:j+x]
                    cv2.imwrite(save_path + image[:-4] + '_' + str(i) + '_' + str(j) + '.jpg', crop)
            try:
                os.remove(save_path + image)
            except:
                pass

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

