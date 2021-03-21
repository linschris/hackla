from flask import Flask, request, redirect, url_for, render_template, session
import json

app = Flask("server")

@app.route('/')
def homeRoute():
    pass