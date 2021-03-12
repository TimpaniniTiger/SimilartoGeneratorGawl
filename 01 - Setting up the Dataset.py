# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:35:25 2021

@author: Connor
"""


import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from tqdm import tqdm
import pickle

filepath = "C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\UserAnimeList.csv"


data = pd.read_csv(filepath,
                   # nrows=1000,
                   usecols=['username', 'anime_id', 'my_score'],
                   dtype={
                       'username': 'str',
                       'anime_id': np.int32,
                       'my_score': np.int8})

# Rows
userlist = list(data['username'].drop_duplicates())
user_index = {username: ind for ind, username in enumerate(userlist)}

# Columns
animelist = list(data['anime_id'].drop_duplicates())
anime_index = {anime_id: ind for ind, anime_id in enumerate(animelist)}

n_rows = len(userlist)  # 283045
n_cols = len(animelist)  # 14478

# Export data to numpy array
data_vec = data.values

### Setup the sparse ratings matrix
# ratings_matrix = csr_matrix((n_rows, n_cols), dtype=np.int8)

# For loop over data rows to fill out ratings_matrix
# # Using DataFrame
# for row in tqdm(data.iterrows(), total=data.shape[0]):
#     row = row[1]
#     ratings_matrix[user_index[row['username']],
#                    anime_index[row['anime_id']]] =\
#         row['my_score']

# for row in tqdm(data_vec, total=data_vec.shape[0]):
#     ratings_matrix[user_index[row[0]],
#                     anime_index[row[1]]] =\
#         row[2]

# Specify sparse ratings_matrix via rows, cols
csr_data = data_vec[:, 2].astype('int8')
csr_row_ind = np.array([user_index[x] for x in data_vec[:, 0]])
csr_col_ind = np.array([anime_index[x] for x in data_vec[:, 1]])
ratings_matrix = csr_matrix((csr_data, (csr_row_ind, csr_col_ind)), shape=(n_rows, n_cols))


### Save to pickle
pickle.dump({'user_index': user_index,
             'anime_index': anime_index,
             'ratings_matrix': ratings_matrix},
            open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\ratings_matrix.pkl", 'wb'))

