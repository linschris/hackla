import json
from dotenv import *
import os
from openfoodfacts import *
import requests
import urllib

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("FDC_API_KEY")

def calculate_initial_nutrients(user):
    sex = user['sex']
    weight = user['weight']
    if sex == "Male":
        nutrients = {
            'protein_remaining' : {
                'min' : 95.0,
                'max' : 165.0,
                'unit' : 'g'
            },
            'calories_remaining' : {
                'min' : (weight * 35.0),
                'max' : (weight * 47.0),
                'unit' : 'kcal'
            },
            'vitamin_c_remaining' : {
                'min' : 75.0,
                'unit' : 'mg'
            },
            'vitamin_d_remaining' : {
                'min' : 15.0,
                'unit' : 'mcg'
            },
            'zinc_remaining' : {
                'min' : 11.0,
                'unit' : 'mg'
            },
            'calcium_remaining' : {
                'min' : 1000.0,
                'max' : 1200.0,
                'unit' : 'mg'
            },
            'iron_remaining' : {
                'min' : 8.7,
                'unit' : 'g'
            },
            'vitamin_a_remaining' : {
                'min' : 900,
                'unit' : 'mcg'
            }
        }

    elif sex == "Female":
        nutrients = {
            'calories_remaining' : {
                'min' : weight * 35.0,
                'max' : weight * 47.0,
                'unit' : 'kcal'
            },
            'protein_remaining' : {
                'min' : 95.0,
                'max' : 165.0,
                'unit' : 'g'
            },
            'vitamin_c_remaining' : {
                'min' : 95.0,
                'unit' : 'mg'
            },
            'zinc_remaining' : {
                'min' : 8.0,
                'unit' : 'mg'
            },
            'vitamin_d_remaining' : {
                'min' : 15.0,
                'unit' : 'mcg'
            },        
            'calcium_remaining' : {
                'min' : 1000.0,
                'max' : 1200.0,
                'unit' : 'mg'
            },
            'iron_remaining' : {
                'min' : 14.8,
                'unit' : 'g'
            },
            'vitamin_a_remaining' : {
                'min' : 700,
                'unit' : 'mcg'
            }
        }
    return nutrients

def search_items(query):
    response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + SECRET_KEY + '&query=' + query)
    response.encoding = 'utf-8'
    return response

def update_nutrients(item, nutrients, modifier=1):
    m = modifier
    item['proteins'] *= m
    nutrients['protein_remaining']['min'] -= item['proteins']
    nutrients['protein_remaining']['max'] -= item['proteins']
    
    item['calories'] *= m
    nutrients['calories_remaining']['min'] -= item['calories']
    nutrients['calories_remaining']['max'] -= item['calories']
    
    item['vitamin_c'] *= m
    nutrients['vitamin_c_remaining']['min'] -= item['vitamin_c']
    
    # item['zinc'] *= m    
    # nutrients['zinc_remaining']['min'] -= item['zinc']
    
    item['vitamin_d'] *= m
    nutrients['vitamin_d_remaining']['min'] -= item['vitamin_d']
    
    item['calcium'] *= m
    nutrients['calcium_remaining']['min'] -= item['calcium']
    nutrients['calcium_remaining']['max'] -= item['calcium']
    
    item['iron'] *= m
    nutrients['iron_remaining']['min'] -= item['iron']
    
    item['vitamin_a'] *= m
    nutrients['vitamin_a_remaining']['min'] -= item['vitamin_a']
    
    return nutrients

def fetch_item_barcode(barcode):
    product = openfoodfacts.products.get_product(barcode)["product"]
    item = {}
    item['calories']  = product["nutriments"]["energy-kcal"]
    item['proteins']  = product["nutriscore_data"]["proteins_value"] if ('proteins_value'  in product["nutriscore_data"]) else 0
    item['vitamin_c'] = product["nutriments"]["vitamin-c_value"]     if ('vitamin-c_value' in product["nutriments"])      else 0
    item['vitamin_d'] = product["nutriments"]["vitamin-d_value"]     if ('vitamin-d_value' in product["nutriments"])      else 0
    item['calcium']   = product["nutriments"]["calcium_value"]       if ('calcium_value'   in product["nutriments"])      else 0
    item['iron']      = product["nutriments"]["iron_value"]          if ('iron_value'      in product["nutriments"])      else 0
    item['vitamin_a'] = product["nutriments"]["vitamin-a_value"]     if ('vitamin-a_value' in product["nutriments"])      else 0
    return item

def fetch_item_fdcid(fdcid):
    product = requests.get('https://api.nal.usda.gov/fdc/v1/food/' + fdcid + '?api_key=' + SECRET_KEY)
    product = product.json()
    item = {}
    NUTRIENT_LIST = {
        "Energy": "calories",
        "Protein": "proteins",
        "Vitamin C, total ascorbic acid" : "vitamin_c",
        "Calcium, Ca" : "calcium",
        "Vitamin D (D2 + D3), International Units" : "vitamin_d",
        "Iron, Fe" : "iron",
        "Vitamin A, IU" : "vitamin_a",
    
    }
    for entry in product["foodNutrients"]:
        nutrient = entry['nutrient']
        if nutrient['name'] in NUTRIENT_LIST:
            if(nutrient['name'] == "Vitamin D (D2 + D3), International Units"):
                entry['amount'] /= 40
            item[NUTRIENT_LIST[nutrient['name']]] = entry["amount"]
    
    return item

def add_item_barcode(barcode, nutrients):
    item = fetch_item_barcode(barcode)    
    return update_nutrients(item, nutrients)

def add_item_fdcid(fdcid, nutrients):
    item = fetch_item_fdcid(fdcid)
    return update_nutrients(item, nutrients)

def delete_item_barcode(barcode, nutrients):
    item = fetch_item_barcode(barcode)
    return update_nutrients(item, nutrients, -1)

def delete_item_fdcid(fdcid, nutrients):
    item = fetch_item_fdcid(fdcid)
    return update_nutrients(item, nutrients, -1)