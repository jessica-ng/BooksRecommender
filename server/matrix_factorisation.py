import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

def load_data(user_id):
    book_titles = pd.read_csv("data/books.csv", sep=',')

    ratings = pd.read_csv("data/new_ratings.csv", sep=',')

    book_data = pd.merge(book_titles, ratings, on='id')

    r_df = pd.pivot_table(book_data, index = 'user_id', columns ='book_id', values = 'rating').fillna(0)

    user = r_df.loc[user_id]
    user = pd.DataFrame(user)

    user = pd.DataFrame(user[user.sum(axis=1) != 0])

    user_full = (book_titles.merge(user, how = 'left', left_on = 'book_id', right_on = 'book_id'))
   
    print(user_full)

    r = r_df.as_matrix()

    user_ratings_mean = np.mean(r, axis = 1)
    r_demeaned = r - user_ratings_mean.reshape(-1, 1)

    U, sigma, Vt = svds(r_demeaned, k = 50)
    sigma = np.diag(sigma)

    ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    preds_df = pd.DataFrame(ratings, columns = r_df.columns)

    user_pred = preds_df.loc[user_id]

    print(pd.DataFrame(user_pred).sort_values(user_id, ascending = False))

    recommendations = (book_titles[~book_titles['book_id'].isin(user.index)].
        merge(user_pred.reset_index(), how = 'left',
            left_on = 'book_id',
            right_on = 'book_id').sort_values(user_id, ascending = False))

    print(recommendations.head(10))
    return recommendations.head(25)

def filter(recommendations):
    book_genres = pd.read_csv("data/book_genres.csv", sep=',')

    filtered = pd.merge(recommendations, book_genres, on='book_id')

    print(filtered)

    print(filtered.loc[filtered['genres'].str.contains('young-adult', na=False)])
