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

def get_fdcid_info(fdcid):
    product = requests.get('https://api.nal.usda.gov/fdc/v1/food/' + fdcid + '?api_key=' + SECRET_KEY)
    product = product.json()
    NUTRIENT_LIST = {
        "Energy": "calories",
        "Protein": "proteins",
        "Vitamin C, total ascorbic acid" : "vitamin_c",
        "Calcium, Ca" : "calcium",
        "Vitamin D (D2 + D3), International Units" : "vitamin_d",
        "Vitamin D (D2 + D3)" : "vitamin_d",
        "Iron, Fe" : "iron",
        "Vitamin A, IU" : "vitamin_a",
        "Vitamin A, RAE" : "vitamin_a"
    }
    product_info = {
        "code": product.get("fdcId"),
        "type": "fdcid",
        "product": {
            "generic_name": product.get("description"),
            "product_name": product.get("description"), #both same
            # "quantity": fdcid doesn't have product quantity
            "brands": product.get("brandOwner"),
            "serving_quantity": product.get("servingSize"),
            "serving_quantity_unit" : product.get("servingSizeUnit"),
            "nutriments" : {
                "calories" : 0,
                "proteins" : 0,
                "vitamin_c" : 0,
                "vitamin_d" : 0,
                "calcium" : 0,
                "iron" : 0,
                "vitamin_a" : 0
                },
            "units" : {
                "calories": "Cal",
                "proteins" : "",
                "vitamin_c" : "",
                "vitamin_d" : "mcg",
                "calcium" : "",
                "iron" : "mg",
                "vitamin_a" : "mcg"
                }
            }
        }
    for entry in product["foodNutrients"]:
        nutrient = entry['nutrient']
        if nutrient['name'] in NUTRIENT_LIST:
            if(nutrient['name'] == "Vitamin D (D2 + D3), International Units"):
                entry['amount'] /= 40
            if(nutrient['name'] == "Vitamin A, IU"):
               entry['amount'] /= 1.5
            product_info['product']['nutriments'][NUTRIENT_LIST[nutrient['name']]] = entry['amount']
            if(nutrient['name'] != "Energy" and nutrient['name'] != "Vitamin D (D2 + D3), International Units" and nutrient['name'] != "Vitamin A, IU"):
                product_info['product']['units'][NUTRIENT_LIST[nutrient['name']]] = entry['nutrient']['unitName']
    return product_info

def update_nutrients(item, nutrients, modifier=1):
    m = modifier
    item['proteins'] = item.get('proteins', 0) * m
    nutrients['protein_remaining']['min'] -= item.get('proteins', 0)
    nutrients['protein_remaining']['max'] -= item.get('proteins', 0)
    
    item['calories'] = item.get('calories', 0) * m
    nutrients['calories_remaining']['min'] -= item.get('calories', 0)
    nutrients['calories_remaining']['max'] -= item.get('calories', 0)
    
    item['vitamin_c'] = item.get('vitamin_c', 0) * m
    nutrients['vitamin_c_remaining']['min'] -= item.get('vitamin_c', 0)
    
    item['vitamin_d'] = item.get('vitamin_d', 0) * m
    nutrients['vitamin_d_remaining']['min'] -= item.get('vitamin_d', 0)
    
    item['calcium'] = item.get('calcium', 0) * m
    nutrients['calcium_remaining']['min'] -= item.get('calcium', 0)
    nutrients['calcium_remaining']['max'] -= item.get('calcium', 0)
    
    item['iron'] = item.get('iron', 0) * m
    nutrients['iron_remaining']['min'] -= item.get('iron', 0)
    
    item['vitamin_a'] = item.get('vitamin_a', 0) * m
    nutrients['vitamin_a_remaining']['min'] -= item.get('vitamin_a', 0)
    
    return nutrients

def fetch_item_barcode(barcode):
    product = openfoodfacts.products.get_product(barcode)["product"]
    item = {}
    item['calories']  = product["nutriments"].get("energy-kcal", 0)
    item['proteins']  = product["nutriments"].get("proteins_value", 0)
    item['vitamin_c'] = product["nutriments"].get("vitamin-c_value", 0)
    item['vitamin_d'] = product["nutriments"].get("vitamin-d_value", 0)
    item['calcium']   = product["nutriments"].get("calcium_value", 0)
    item['iron']      = product["nutriments"].get("iron_value", 0)
    item['vitamin_a'] = product["nutriments"].get("vitamin-a_value", 0)
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
        "Vitamin D (D2 + D3)" : "vitamin_d",
        "Iron, Fe" : "iron",
        "Vitamin A, IU" : "vitamin_a",
        "Vitamin A, RAE" : "vitamin_a"
    }
    for entry in product["foodNutrients"]:
        nutrient = entry['nutrient']
        if nutrient['name'] in NUTRIENT_LIST:
            if(nutrient['name'] == "Vitamin D (D2 + D3), International Units"):
                entry['amount'] /= 40
            if(nutrient['name'] == "Vitamin A, IU"):
                entry['amount'] /= 1.5
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