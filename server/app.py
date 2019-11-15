from flask import Flask, jsonify, request
from flask_cors import CORS

import numpy as np
import pandas as pd
import os
import sys
import csv

import recommendation
global book_data
global ratings_data

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

test_username = 'admin'
test_password = 'password'


# sanity check route
@app.route('/test', methods=['GET'])
def ping_pong():
    recommendation.initiateData()
    return jsonify('pong!')

# validate login
@app.route('/validate', methods=['POST'])
def validate():
    username = request.get_json()['username']
    password = request.get_json()['password']
    app.logger.info(request.args.get('username'))
    if test_username == username and password == test_password:
        return jsonify(True)
    return jsonify(False)

# submit rating
@app.route('/sumbitrating', methods=['POST'])
def submit_rating():
    userId = request.get_json()['userid']
    bookId = request.get_json()['bookid']
    rating = request.get_json()['rating']
    print(userId, bookId, rating)
    recommendation.addRating(userId, bookId, rating)
    return jsonify(True)

if __name__ == '__main__':
    #recommendation.initiateData()
    app.run()

