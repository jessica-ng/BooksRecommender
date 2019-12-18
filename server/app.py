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

global logins
logins = dict()
logins['1000'] = 'password'

# sanity check route
@app.route('/test', methods=['GET'])
def ping_pong():
    recommendation.initiateData()
    return jsonify('pong!')

# validate login
@app.route('/validate', methods=['POST'])
def validate():
    global logins
    username = request.get_json()['username']
    password = request.get_json()['password']
    if username in logins.keys():
        if logins[username] == password:
            return jsonify(True)
    return jsonify(False)

# add new login
@app.route('/sign_up', methods=['POST'])
def signup():
    global logins
    username = request.get_json()['username']
    password = request.get_json()['password']
    logins[str(username)] = password
    
    return jsonify(True)
    

# submit rating
@app.route('/sumbitrating', methods=['POST'])
def submit_rating():
    userId = request.get_json()['userid']
    bookId = request.get_json()['bookid']
    rating = request.get_json()['rating']
    print(userId, bookId, rating)
    recommendation.addRating(userId, bookId, rating)
    return jsonify(True)

#return sample of books for onboarding
@app.route('/get_books', methods=['GET'])
def get_books():
    #recommendation.initiateData()
    books = recommendation.getRandomBooks()
    return books

#return information about all books in the database
@app.route('/get_all_books', methods=['POST'])
def get_all_books():
    user_id = request.get_json()['user_id']
    #recommendation.initiateData()
    books = recommendation.get_all_books(int(user_id))
    return books.to_json()

# return recommendations based on user's previous ratings
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    print("getting recommendations")
    user_id = request.get_json()['user_id']
    books = recommendation.get_recommendations(int(user_id))
    books = recommendation.filter(books, int(user_id))
    return books.to_json(orient='index')

# get user's past ratings
@app.route('/get_ratings', methods=['POST'])
def get_ratings():
    user_id = request.get_json()['user_id']
    ratings = recommendation.getProfile(int(user_id))
    if type(ratings) != type(False):
        return ratings.to_json()
    if ratings == False:
        return jsonify(False)
    return ratings.to_json()

@app.route('/update_ratings', methods=['POST'])
def update_ratings():
    user_id = request.get_json()['user_id']
    book_id = request.get_json()['book_id']
    old_rating = request.get_json()['old_rating']
    new_rating = request.get_json()['new_rating']
    print(user_id, book_id, old_rating, new_rating)
    recommendation.update_ratings(user_id, book_id, old_rating, new_rating)
    return jsonify(True)

@app.route('/new_userid', methods=['GET'])
def new_userid():
    return str(recommendation.new_userid())

@app.route('/initiate', methods=['GET'])
def initiate():
    recommendation.initiateData()
    return jsonify(True)

if __name__ == '__main__':
    recommendation.initiateData()
    app.jinja_env.cache = {}
    app.run()