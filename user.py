class User:
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
        self.proteinGoalMin - self.protein = self.proteinGoalMin
        # self.protein_remaining - 
        self.proteinGoalMax - self.protein = self.proteinGoalMax

    def calories(self):
        self.calorieGoalMin - self.calorie = self.calorieGoalMin
        self.calorieGoalMax - self.calorie = self.calorieGoalMax

    def vitaminC(self):
        if self.sex == "Male":
            if self.vitaminC > 500 or self.vitaminCGoal < -905:
                print("If vitaminC intake is over 500 it's useless and if intake is over 1000 it will harm you")
            else:
                self.vitaminCGoal - self.vitaminC = self.vitaminCGoal
                
        elif self.sex == "Female":
            if self.vitaminC > 500 or self.vitaminCGoal < -925:
                print("If vitaminC intake is over 500 it's useless and if intake is over 1000 it will harm you")
            else:   
                self.vitaminCGoal - self.vitaminC = self.vitaminCGoal

    def zinc(self):
      if self.sex == "Male":
            self.maleZincGoal - self.zinc = self.maleZincGoal
      elif self.sex == "Female":
            self.femaleZincGoal - self.zinc = self.femaleZincGoal

    def vitaminD(self):
        self.vitaminDGoal - self.vitaminD = self.vitaminDGoal

    def calcium(self):
        if self.calcium > 500:
            print ("Calcium intake is too high for one meal")
            self.calciumGoal - 500 = self.calciumGoal
        else:
            self.calciumGoal - self.calcium = self.calciumGoal
        
    def omega3(self):
        if self.sex == "Male":
            self.maleOmega3Goal - self.omega3 = self.maleOmega3Goal
        elif self.sex == "Female":
            self.femaleOmega3Goal - self.omega3 = self.femaleOmega3Goal

p1 = User(40, "Male")
p1.myfunc()

# protein: 105-165 grams of protein a day
# calories: it's a table so we can do by range
# Vitamin C: 95 mg for men, 75 mg for women. 200-500 is ok but anything more than 1k is unhealthy
# Zinc: 11mg for men, 8mg for women
# Vitamin D: 15 mcg 
# Getting in 1000 -1200 mg each day of calcium, also in divided amounts throughout the day, for bone health is imperative. Your body can only absorb 500 mg of calcium at one time.
# Omega-3: women: 1.1g, men: 1.6g

'''
This class has 2 main methods

1. calculate_initial_nutrients(user):
This takes in some user data, and it gets the initial nutrients
user: {
    age: 12,
    sex: "Male",
    weight: 10.4
}
This returns some data about what nutrients are still needed
response: {
"calcium_remaining": 250,
"calcium_unit": "mg",
...
}


2. calculate_remaining_nutrients(current_nutrients, food_item_to_consume): 
This takes in the current remaining nutrients FROM the user, and subtracts the food item's nutrients from the remaining
Then it returns some data about what nutrients are still needed. This is the same format.
response: {
"calcium_remaining": 250,
"calcium_unit": "mg",
...
}
'''



