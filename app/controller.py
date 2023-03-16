from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/crawl', methods = ['POST'])
def index():
    return jsonify({'ok': 200})
    

@app.route('/filter/more_than_five', methods = ['GET'])
def filter_more_than_five():
    return jsonify({'ok': 200})


@app.route('/filter/less_than_or_five', methods = ['GET'])
def filter_less_than_or_five():
    return jsonify({'ok': 200})