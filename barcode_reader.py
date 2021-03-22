from pyzbar import pyzbar
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw
import cv2

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print(obj.rect)
        
    return image

        
def increase_contrast(image):
    img = Image.open(image)
    enhancer = ImageEnhance.Contrast(img)
    factor = 5 #increase contrast
    im_output = enhancer.enhance(factor)
    # im_output.save('more-image.png')
    return im_output



# load the image to opencv

img = increase_contrast('./image3.jpg')
# decode detected barcodes & get the image
# that is drawn
img = decode(img)
# show the image
img.show()
img.close()

# cv2.imshow("img", img)
# cv2.waitKey(0)


