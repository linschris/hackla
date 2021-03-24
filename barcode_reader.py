from pyzbar import pyzbar
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw
from openfoodfacts import *
import json
import io
import base64

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print(obj.rect)
        return (obj.data, obj.rect)


def increase_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    factor = 5 #increase contrast
    im_output = enhancer.enhance(factor)
    # im_output.save('more-image.png')
    return im_output

def get_barcode_num(image):
    # load the image to Pillow
    img = increase_contrast(image)
    # decode detected barcodes & get the image
    # that is drawn
    (barcode_num, barcode_rect) = decode(img)
    return (barcode_num, barcode_rect)

def get_barcode_info(image):
    (barcode_num, barcode_rect) = get_barcode_num(image)
    product = openfoodfacts.products.get_product(barcode_num)
    (top, left, width, height) = barcode_rect
    if(product["status_verbose"] != "product not found"):
        product_info = {
        "code": product["code"],
        "box": {
            "left": left,
            "top": top,
            "width": width,
            "height": height
        },
        "product": {
            "generic_name": product["product"]["generic_name_en"],
            "quantity": product["product"]["quantity"],
            "brands": product["product"]["brands"],
            "nutriscore_grade": product["product"]["nutriscore_grade"],
            "nova_group": product["nova_groups"]
            }
        }
    else:
        product_info = {}
    return product_info
