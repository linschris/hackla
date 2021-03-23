import json
from dotenv import *
import os
from openfoodfacts import *
import requests
import urllib


load_dotenv(find_dotenv())


SECRET_KEY = os.getenv("FDC_API_KEY")

# class User:
    CONST_CALORIE_MULTIPLIER_35 = 35.0
    CONST_CALORIE_MULTIPLIER_47 = 47.0
    weight = 0.0
    sex = ""
    CONST_M = "Male"
    CONST_F = "Female"
    #cal
    calories = 0.0

    calorieGoalMin = 0.0
    calorieGoalMax = 0.0

    #g
    protein = 0.0
    proteinGoalMin = 95.0
    proteinGoalMax = 165.0
    
    #mg
    vitaminC = 0.0
    vitaminCGoal = 0.0

    #mg
    zinc = 0.0
    zincGoal = 0.0 

    #micrograms
    vitaminD = 0.0
    vitaminDGoal = 15.0 

    #mg
    iron = 0.0
    ironGoal = 8.7
    
    #User constructor
    def __init__(self, weight, sex):
        if (weight < 0.0 ):
            self.weight = weight
        else:
            print("Invalid Weight!")
        if (sex.lower() == "male" or sex.lower() == "female" ):
            self.sex = sex
        else:
            print("Invalid Sex!")    
    # CalorieGoal setter and getter functions
    def setCalorieGoal(self):
        calorieGoalMin = self.weight * self.CONST_CALORIE_MULTIPLIER_35
        calorieGoalMax = self.weight * self.CONST_CALORIE_MULTIPLIER_47
    def getCalorieGoalMin(self):
        return self.calorieGoalMin
    def getCalorieGoalMax(self):
        return self.calorieGoalMax
    # Protein Goal getter functions, no need for setter because it doesn't vary
    def getProteinGoalMin(self):
        return self.proteinGoalMin
    def getProteinGoalMax(self):
        return self.proteinGoalMax
    # Vitamin C Goal setter and getter functions
    def setVitaminCGoal(self):
        if (self.sex == self.CONST_M):
            self.vitaminCGoal = 95.0
        if (self.sex == self.CONST_F):
            self.vitaminCGoal = 75.0
    def getVitaminCGoal(self):
        return self.vitaminCGoal
    # Zinc Goal setter and getter function
    def setZincGoal(self):
        if (self.sex == self.CONST_M):
            self.zincGoal = 11.0
        if (self.sex == self.CONST_F):
            self.zincGoal = 8.0
    def getZincGoal(self):
        return self.zincGoal
    # Vitamin D goal getter function, setter not necessary
    def getVitaminDGoal(self):
        return self.vitaminDGoal

    def myfunc(self):
        print("Hello my sex is " + self.sex)
    
    def protein(self):
        self.proteinGoalMin = self.proteinGoalMin - self.protein
        # self.protein_remaining - 
        self.proteinGoalMax = self.proteinGoalMax - self.protein

    def calories(self):
        self.calorieGoalMin = self.calorieGoalMin - self.calorie
        self.calorieGoalMax = self.calorieGoalMax - self.calorie 

    def vitaminC(self):
        if self.sex == "Male":
            if self.vitaminC > 500 or self.vitaminCGoal < -1105:
                print("If vitaminC intake is over 500 it's useless and if intake is over 1200 it will harm you")
            else:
                self.vitaminCGoal = self.vitaminCGoal - self.vitaminC 
                
        elif self.sex == "Female":
            if self.vitaminC > 500 or self.vitaminCGoal < -1125:
                print("If vitaminC intake is over 500 it's useless and if intake is over 1200 it will harm you")
            else:   
                self.vitaminCGoal = self.vitaminCGoal - self.vitaminC

    def zinc(self):
      if self.sex == "Male":
            self.maleZincGoal = self.maleZincGoal - self.zinc
      elif self.sex == "Female":
            self.femaleZincGoal = self.femaleZincGoal - self.zinc

    def vitaminD(self):
        self.vitaminDGoal = self.vitaminDGoal - self.vitaminD

    def calcium(self):
        if self.calcium > 500:
            print ("Calcium intake is too high for one meal")
            self.calciumGoal = self.calciumGoal - 500
        else:
            self.calciumGoal = self.calciumGoal - self.calcium
        
    def iron(self):
        if self.sex == "Male":
            self.maleIronGoal = self.maleIronGoal - self.iron
        elif self.sex == "Female":
            self.femaleIronGoal = self.femaleIronGoal - self.iron
    
    def vitamin_a(self):
        if self.sex == "Male":
            self.maleVitaminAGoal = self.maleVitaminAGoal - self.vitaminA
        elif self.sex == "Female":
            self.femaleVitaminAGoal = self.femaleVitaminAGoal - self.vitaminA

def calculate_initial_nutrients(user):
    sex = user["sex"]
    weight = user["weight"]
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
                'min' : 11.0
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
    return json.dumps(nutrients)

# def get_barcode_data(barcode):
#     pass

def search_items(query):
    response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + SECRET_KEY + '&query=' + urllib.urlencode(query))
    itemList = []
     

    pass

def update_nutrients(item, nutrients, modifier=1):
    m = modifier
    item['proteins'] * m
    nutrients['protein_remaining'][min] -= item['proteins']
    nutrients['protein_remaining'][max] -= item['proteins']
    
    item['calories'] * m
    nutrients['calories_remaining'][min] -= item['calories']
    nutrients['calories_remaining'][max] -= item['calories']
    
    item['vitamin_c'] * m
    nutrients['vitamin_c_remaining'][min] -= item['vitamin_c']
    
    item['zinc'] * m    
    nutrients['zinc_remaining'][min] -= item['zinc']
    
    item['vitamin_d'] * m
    nutrients['vitamin_d_remaining'][min] -= item['vitamin_d']
    
    item['calcium'] * m
    nutrients['calcium_remaining'][min] -= item['calcium']
    nutrients['calcium_remaining'][max] -= item['calcium']
    
    item['iron'] * m
    nutrients['iron_remaining'][min] -= item['iron']
    
    item['vitamin_a'] * m
    nutrients['vitamin_a_remaining'][min] -= item['vitamin_a']
    
    return json.dumps(nutrients)

def fetch_item_barcode(barcode):
    response = requests.get("https://world.openfoodfacts.org/data/data-fields.txt")
    product = openfoodfacts.products.get_product(barcode)["product"]
    item = {}
    item['calories']  = product["nutriments"]["energy-kcal"]
    item['proteins']  = product["nutriscore_data"]["proteins"] if ('proteins'  in product["nutriscore_data"]) else 0
    item['vitamin_c'] = product["nutriments"]["vitamin-c"]     if ('vitamin-c' in product["nutriments"])      else 0
    item['vitamin_d'] = product["nutriments"]["vitamin-d"]     if ('vitamin-d' in product["nutriments"])      else 0
    item['calcium']   = product["nutriments"]["calcium"]       if ('calcium'   in product["nutriments"])      else 0
    item['iron']      = product["nutriments"]["iron"]          if ('iron'      in product["nutriments"])      else 0
    item['vitamin_a'] = product["nutriments"]["vitamin-a"]     if ('vitamin-a' in product["nutriments"])      else 0
    return item

def add_item_barcode(barcode, nutrients):
    item = fetch_item_barcode(barcode)    
    return update_nutrients(item, nutrients)

# def add_item_fdcid(item):
#     return json.dumps(nutrients)
#     pass

def delete_item_barcode(barcode, nutrients):
    item = fetch_item_barcode(barcode)
    return update_item(item, nutrients, -1)

# def delete_item_fdcid(item):
#     return json.dumps(nutrients)
#     pass

# barcode for coke is "5449000000996"
print(fetch_item_barcode("737628064502"))