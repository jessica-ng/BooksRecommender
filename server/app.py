from flask import Flask, jsonify, request
from flask_cors import CORS

import numpy as np
import pandas as pd
import os
import sys
import csv

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
    return jsonify('pong!')

# sanity check route
@app.route('/validate', methods=['POST'])
def validate():
    username = request.get_json()['username']
    password = request.get_json()['password']
    app.logger.info(request.args.get('username'))
    if test_username == username and password == test_password:
        return jsonify(True)
    return jsonify(False)

if __name__ == '__main__':
    app.run()



def initData():
    current_path = os.path.dirname(os.path.abspath(__file__))

    #encoding = 'unicode_escape'
    ratings_data = pd.read_csv("data/ratings.csv")
    print(ratings_data.head())

    books_data = pd.read_csv("data/book_tags.csv", sep=',')

    book_titles = pd.read_csv("data/books.csv", sep=',')

    print(books_data.head())

    book_data = pd.merge(book_titles, ratings_data, on='book_id')

    tags_data = pd.read_csv("data/tags.csv")

    genre_data = pd.merge(books_data, tags_data, on='tag_id')

    print(book_data)