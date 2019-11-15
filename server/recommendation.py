import numpy as np
import pandas as pd
import os
import sys
import csv

global book_data
global ratings_data
global book_titles


def initiateData():
    current_path = os.path.dirname(os.path.abspath(__file__))

    #encoding = 'unicode_escape'
    ratings_data = pd.read_csv("data/ratings.csv")
    print(ratings_data.head())

    books_data = pd.read_csv("data/book_tags.csv", sep=',')

    global book_titles 
    book_titles= pd.read_csv("data/books.csv", sep=',')

    print(books_data.head())

    book_data = pd.merge(book_titles, ratings_data, on='book_id')

    tags_data = pd.read_csv("data/tags.csv")

    genre_data = pd.merge(books_data, tags_data, on='tag_id')

    print(book_data)

    user_book_rating = book_data.pivot_table(index='user_id', columns='title', values='rating')

    #user_book_rating.dropna(inplace=True)

    print(user_book_rating.head())

    return user_book_rating

def getRecommendations():
    user_book_rating = initiateData()

    test_ratings = user_book_rating["Zodiac"]

    print(test_ratings.head())

    #test_ratings = test_ratings.to_frame()

    book_like_test = user_book_rating.corrwith(test_ratings)

    corr_test= pd.DataFrame(book_like_test, columns=['Correlation'])

    corr_test.dropna(inplace=True)

    print(corr_test.head())

    print(corr_test.sort_values('Correlation', ascending=False).head(10))

def getProfile(userId):
    ratings_data = pd.read_csv("data/ratings.csv")

    book_data = pd.merge(book_titles, ratings_data, on='book_id')

    user_book_rating = book_data.pivot_table(index='title', columns='user_id', values='rating')

    print(user_book_rating)

    profile = user_book_rating[userId]

    profile.dropna(inplace=True)

    print(profile)

    return

def addRating(userId, bookId, rating):
    initiateData()

    fields = [bookId, userId, rating]
    with open('data/ratings.csv', mode='a') as ratings_file:
        
        writer = csv.writer(ratings_file)
        writer.writerow(fields)
    ratings_file.close()

    updateData()

    return

def updateData():
    ratings_data = pd.read_csv("data/ratings.csv")

    book_data = pd.merge(book_titles, ratings_data, on='book_id')

    return


def main():
    getProfile(11)

    addRating(11, 5, 3)
    
    getProfile(11)

if __name__ == '__main__':
    main()