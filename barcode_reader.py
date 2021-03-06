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
        return (obj.data, obj.rect)

def increase_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    contrast_factor = 5
    im_output = enhancer.enhance(contrast_factor)
    return im_output

def get_barcode_num(image):
    # load the image to Pillow
    barcode_img = increase_contrast(image)
    # decode detected barcodes & get the image
    # that is drawn
    return decode(barcode_img)

def get_barcode_info(image):
    try:
        (barcode_num, barcode_rect) = get_barcode_num(image)
    except TypeError:
        return { "error": "Barcode not detected", "code": 400 }
    product = openfoodfacts.products.get_product(str(barcode_num))
    (top, left, width, height) = barcode_rect
    if(product["status_verbose"] != "product not found"):
        product_info = {
        "code": product["code"],
        "type": "barcode",
        "box": {
            "left": left,
            "top": top,
            "width": width,
            "height": height
        },
        "product": {
            "generic_name": product["product"].get("generic_name_en"),
            "product_name": product["product"].get("product_name"),
            "quantity": product["product"].get("quantity"),
            "brands": product["product"].get("brands"),
            "nutriscore_grade": product["product"].get("nutriscore_grade"),
            "nova_group": product["product"].get("nova_groups"),
            "serving_quantity": product["product"].get("serving_quantity"),
            "nutriments" : {
                "calories" : product["product"]["nutriments"].get("energy-kcal"),
                "proteins" : product["product"]["nutriments"].get("proteins_value"),
                "vitamin_c" : product["product"]["nutriments"].get("vitamin-c_value"),
                "vitamin_d" : product["product"]["nutriments"].get("vitamin-d_value"),
                "calcium" : product["product"]["nutriments"].get("calcium_value"),
                "iron" : product["product"]["nutriments"].get("iron_value"),
                "vitamin_a" : product["product"]["nutriments"].get("vitamin-a_value")
                },
            "units" : {
                "calories": "Cal",
                "proteins" : product["product"]["nutriments"].get("proteins_unit"),
                "vitamin_c" : product["product"]["nutriments"].get("vitamin-c_unit"),
                "vitamin_d" : product["product"]["nutriments"].get("vitamin-d_unit"),
                "calcium" : product["product"]["nutriments"].get("calcium_unit"),
                "iron" : product["product"]["nutriments"].get("iron_unit"),
                "vitamin_a" : product["product"]["nutriments"].get("vitamin-a_unit")
                }
            }
        }
    
    else:
        product_info = {}
    return product_info