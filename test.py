#!/usr/bin/env python3

from rawkit.raw import Raw 
from PIL import Image
import rawpy
import cv2

with Raw('DSC02580.ARW') as rw:
    # print(rw.metadata)
    exif = rw.metadata

# with rawpy.imread('DSC02580.ARW') as rw:
#     rgb = rw.postprocess()
# cv2.imwrite('test.jpg', rgb)
# exif = bytes(exif)
print(exif)
eee = str(exif).split(b'\x00')
print(eee)
# image_new = Image.open('test.jpg')
# image_new.save('test_w_EXIF.jpg', 'JPEG', exif=exif)



# # read exif from new image
# image_ew = Image.open('test_w_EXIF.jpg')
# exif_new = image_ew.info['exif']
# print(exif_new)
