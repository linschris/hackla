from flask import Flask, request, redirect, url_for, render_template, session
from dotenv import *
import os

import json
load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("FDC_KEY")


app = Flask("server")



@app.route('/')
def homeRoute():
    pass