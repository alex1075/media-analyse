#!/usr/bin/env python3
import os
from subprocess import check_output
import cv2
import tqdm

def read_metadata(image):
    ut = []
    out = check_output(['iinfo' , image, '-v'])
    out = out.decode('utf-8').split('\n')
    for line in out:
        ut.append(line.replace('    ', ''))
    ut.pop(0)
    ut.pop(0)
    ut.pop(-1)
    return ut

def add_metadata(image, metadata):
    for line in metadata:
        line = line.split(': ')
        if line[0] == 'Make':
            os.system('oiiotool ' + image + ' --attrib "Make" "' + line[1] + '" --nosoftwareattrib -o ' + image)
        elif line[0] == 'Model':
            os.system('oiiotool ' + image + ' --attrib "Model" "' + line[1] + '" --nosoftwareattrib -o ' + image)
        elif line[0] == 'ExposureTime':
            os.system('oiiotool ' + image + ' --attrib "ExposureTime" ' + str(line[1]) + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'FNumber':
            os.system('oiiotool ' + image + ' --attrib "FNumber" "' + line[1] + '" --nosoftwareattrib -o ' + image)
        elif line[0] == 'Orientation':
            test = line[1]
            os.system('oiiotool ' + image + ' --attrib "Orientation" ' + test[0] + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:ApertureValue':
            test = line[1].split(' ')
            os.system('oiiotool ' + image + ' --attrib "Exif:ApertureValue" ' + str(test[0]) + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:BrightnessValue':    
            test = line[1].split(' ')
            test = test[1].split('(')
            test = test[1]
            # print(test)
            os.system('oiiotool ' + image + ' --attrib "Exif:BrightnessValue" ' + test[:-1] + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:ColorSpace':
            os.system('oiiotool ' + image + ' --attrib "Exif:ColorSpace" ' + line[1] + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:ExposureMode':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:ExposureMode" ' + test + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:ExposureProgram':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:ExposureProgram" ' + test + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:Flash':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:Flash" ' + test + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:FocalLength':
            test = line[1].split(' ')
            test = f"{float(test[0]):.1f}"
            os.system('oiiotool ' + image + ' --attrib "Exif:FocalLength" ' + str(test) + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:ISOSpeedRatings':
            os.system('oiiotool ' + image + ' --attrib "Exif:ISOSpeedRatings" ' + line[1] + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:MeteringMode':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:MeteringMode" ' + test + ' --nosoftwareattrib -o ' + image) 
        elif line[0] == 'Exif:LightSource':  
            test = line[1].split(' ') 
            os.system('oiiotool ' + image + ' --attrib "Exif:LightSource" ' + test + ' --nosoftwareattrib -o ' + image) 
        elif line[0] == 'Exif:MaxApertureValue':
            test = line[1].split(' ')
            test = test[1].split('(')
            test = test[1]
            test = test[:-1]
            os.system('oiiotool ' + image + ' --attrib "Exif:MaxApertureValue" ' + test + ' --nosoftwareattrib -o ' + image) 
        elif line[0] == 'PixelAspectRatio':
            os.system('oiiotool ' + image + ' --attrib "PixelAspectRatio" ' + line[1] + ' --nosoftwareattrib -o ' + image) 
        elif line[0] =='Exif:Contrast':
            test = line[1].split(' ')
            test = test[1].split('(')
            test = test[1]
            test = test[:-1]
            os.system('oiiotool ' + image + ' --attrib "Exif:Contrast" ' + test + ' --nosoftwareattrib -o ' + image)  
        elif line[0] == 'Exif:Saturation':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:Saturation" ' + test + ' --nosoftwareattrib -o ' + image) 
        elif line[0] == 'Exif:SceneCaptureType':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:SceneCaptureType" ' + test + ' --nosoftwareattrib -o ' + image)
        elif line[0] == 'Exif:Sharpness':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:Sharpness" ' + test + ' --nosoftwareattrib -o ' + image)   
        elif line[0] == 'Exif:ShutterSpeedValue':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:ShutterSpeedValue" ' + test + ' --nosoftwareattrib -o ' + image)  
        elif line[0] == 'Exif:WhiteBalance':
            test = line[1].split(' ')
            test = test[0]
            os.system('oiiotool ' + image + ' --attrib "Exif:WhiteBalance" ' + test + ' --nosoftwareattrib -o ' + image)        
        else:
            pass

def prepare_exif_donor_image(image1, image2, formati='.jpg'):
    width, height, _ = cv2.imread(image2).shape
    image_out = image1.split('.')
    image_out = image_out[0] + formati
    print(width, height)
    os.system('oiiotool ' + image1 + ' -resize ' + str(height) + 'x' + str(width) + ' -o ' + image_out)
    return image_out    

def copy_metadata(image1, image2):
    image1 = prepare_exif_donor_image(image1, image2)
    os.system('oiiotool ' + image1 + ' ' + image2 + ' --pastemeta --nosoftwareattrib -o ' + image2)

def iterate_meta_copy(folder, image1):
    for image in tqdm.tqdm(os.listdir(folder), desc='Copying metadata'):
        if image.endswith('.jpg'):
            copy_metadata(image1, folder + '/' + image)