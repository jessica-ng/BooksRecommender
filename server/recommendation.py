import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
import os
import sys
import csv

global book_data
global ratings_data
global book_titles
global book_genres


def initiateData():
    current_path = os.path.dirname(os.path.abspath(__file__))
    clean_ratings()

    global ratings_data
    ratings_data = pd.read_csv("data/new_ratings2.csv")

    global book_titles
    book_titles = pd.read_csv("data/books.csv", sep=',')

    global book_data
    book_data = pd.merge(book_titles, ratings_data, on='id')

    global book_genres
    book_genres = pd.read_csv("data/book_genres.csv", sep=',')

    user_book_rating = book_data.pivot_table(
        index='user_id', columns='title', values='rating')

    return user_book_rating


def getProfile(userId):
    try:
        clean_ratings()
        ratings_data = pd.read_csv("data/new_ratings2.csv")

        global book_titles
        book_data = pd.merge(book_titles, ratings_data, on='id')

        user_book_rating = pd.pivot_table(
            book_data, index='user_id', columns='book_id', values='rating').fillna(0)
        user_book_rating = user_book_rating.loc[userId]
        user_book_rating = pd.DataFrame(user_book_rating)
        user_book_rating = pd.DataFrame(user_book_rating[user_book_rating.sum(axis=1) != 0])

        user_book_rating = pd.merge(book_titles, user_book_rating, on='book_id')

    except:
        return False

    return user_book_rating


def addRating(userId, bookId, rating):
    initiateData()

    fields = [bookId, userId, rating]
    with open('data/new_ratings2.csv', mode='a') as ratings_file:

        writer = csv.writer(ratings_file)
        writer.writerow(fields)
    ratings_file.close()

    updateData()
    clean_ratings()

    return


def updateData():
    ratings_data = pd.read_csv("data/new_ratings2.csv")
    global book_data
    global book_titles

    book_data = pd.merge(book_titles, ratings_data, on='id')

    return


def getRandomBooks():
    global book_titles
    sample = book_titles.sample(8)
    return sample.to_json()

def clean_ratings():
    lines = []
    with open('data/new_ratings2.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row == ['','','']:
                continue     
            else:
                lines.append(row)
    readFile.close()
    df = pd.DataFrame(lines[1:], columns=lines[0])
    df.to_csv("data/new_ratings2.csv", sep=',',index=False)
    return


def get_recommendations(user_id):
    #try:
    global book_titles
    global ratings_data
    global book_data

    ratings = ratings_data

    r_df = pd.pivot_table(book_data, index='user_id',
                        columns='book_id', values='rating').fillna(0)

    user = r_df.loc[user_id]
    user = pd.DataFrame(user)

    user = pd.DataFrame(user[user.sum(axis=1) != 0])

    r = r_df.values

    user_ratings_mean = np.mean(r, axis=1)
    r_demeaned = r - user_ratings_mean.reshape(-1, 1)

    U, sigma, Vt = svds(r_demeaned, k=100)
    sigma = np.diag(sigma)

    ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    
    preds_df = pd.DataFrame(ratings, columns=r_df.columns)

    user_pred = preds_df.loc[user_id]

    user_pred = pd.DataFrame(user_pred).sort_values(user_id, ascending=False)

    user_pred = user_pred.head(30)

    book_titles2 = book_titles.copy()
    book_titles2.set_index('book_id', inplace=True)
    user_pred = book_titles2.join(user_pred, how='left').dropna()

    recommendations = (user_pred[~user_pred.index.isin(user.index)].
        merge(user_pred.reset_index(), how='left',
            left_on='book_id',
            right_on='book_id').sort_values(str(user_id)+"_y", ascending=False))

    # except:
    #     print("error")
    #     return 
    #filter(recommendations, user_id)
    return recommendations


def filter(recommendations, user_id):
    global book_genres
    counts = dict()
    ratings = getProfile(user_id)
    ratings = pd.merge(ratings, book_genres, on='book_id')
    genres = list(ratings['genres'])

    for i in range(len(genres)):
        genre = genres[i].split(', ')
        for g in genre:
            if g[1:-1] not in counts.keys():
                counts[g[1:-1]] = 1
            else:
                counts[g[1:-1]] += 1

    sorted_counts = []
    for key, value in sorted(counts.items(), key=lambda item: item[1]):
        sorted_counts.append(key)
    sorted_counts = sorted_counts[::-1]

    filtered = pd.merge(recommendations, book_genres, on='book_id')

    filtered = filtered.loc[filtered['genres'].str.contains(sorted_counts[0], na=False) | filtered['genres'].str.contains(sorted_counts[1], na=False)]

    if len(filtered) < 6:
        return recommendations
    return filtered


def get_all_books(user_id):
    try:
        global book_data
        global book_titles
        r_df = pd.pivot_table(book_data, index='user_id',
                            columns='book_id', values='rating').fillna(0)

        user = r_df.loc[user_id]
        user = pd.DataFrame(user)

        user = pd.DataFrame(user[user.sum(axis=1) != 0])
        books = book_titles[~book_titles['book_id'].isin(user.index)]
    except:
        return book_titles
    return books


def update_ratings(user_id, book_id, old_rating, new_rating):
    lines = []
    delete = [str(book_id), str(user_id), str(old_rating)]
    new = [str(book_id), str(user_id), str(new_rating)]
    with open('data/new_ratings2.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row == ['','','']:
                continue
            elif row != delete:
                lines.append(row)       
            else:
                lines.append(new)
    readFile.close()
    df = pd.DataFrame(lines[1:], columns=lines[0])
    df.to_csv("data/new_ratings2.csv", sep=',',index=False)
    initiateData()

def new_userid():
    global ratings_data
    global book_data

    ratings = ratings_data

    r_df = pd.pivot_table(book_data, index='user_id',
                        columns='book_id', values='rating').fillna(0)
    
    return r_df.index[-1] + 1

            

def main():
    initiateData()
    new_userid()

if __name__ == '__main__':
    main()
