from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from dotenv import *
from user import *
import os

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("FDC_KEY")

app = Flask("server")

@app.route('/calculate/initial', methods=['POST'])
def calculate_initial(user):
    nutrients = calculate_initial_nutrients(user)
    return jsonify(nutrients)

@app.route('/item/barcode', methods=['GET'])
def get_barcode_info(barcode):
    item_info = get_barcode_data(barcode)
    return jsonify(item_info)

@app.route('/item/search', methods=['GET'])
def search(item):
    item = request.args.get('query')
    item_list = search_items(item)
    return jsonify(item_list)

@app.route('/item/fetch', methods=['POST'])
def add_item(item, nutrients):
    if item.request.json['food']['type'] == "barcode":
        nutrients = add_item_barcode(item)
    elif item.request.json['food']['type'] == "fdcid":
        nutrients = add_item_fdcid(item)
    return jsonify(nutrients)

@app.route('/item/delete', methods=['POST'])
def delete_item(item, nutrients):
    if item.request.json['food']['type'] == "barcode":
        nutrients = delete_item_barcode(item)
    elif item.request.json['food']['type'] == "fdcid":
        nutrients = delete_item_fdcid(item)
    return jsonify(nutrients)