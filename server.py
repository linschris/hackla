from flask import Flask, request, redirect, url_for, render_template, session
from dotenv import *
from user import *
import os
import json

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("FDC_KEY")

app = Flask("server")

@app.route('/calculate/initial', methods=['POST'])
def calculate_initial(user):
    initial = calculate_initial_nutrients(user)
    #return json.dumps(inital)
    return initial

@app.route('/calculate/remaining', methods=['POST'])
def calculate_remaining(current_nutrients, food_item_to_consume):
    remaining = calculate_remaining_nutrients(current_nutrients, food_item_to_consume)
    #return json.dumps(remaining)
    return remaining