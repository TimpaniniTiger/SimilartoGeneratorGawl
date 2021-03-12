# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:51:38 2021

@author: Connor
"""


import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from tqdm import tqdm
import pickle

filepath = "C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\UserAnimeList.csv"


# data = pd.read_csv(filepath,
#                     # nrows=100000,  # 80 mil total rows
#                     usecols=['username', 'my_last_updated', 'anime_id'])

# # anime_id ordered by last updated time
# data[data['username'] == data.iloc[0]['username']].sort_values(by='my_last_updated')['anime_id']

""" Idea is to make a "sentence" of a user's anime rating order, train a
word2vec embedding on these sentences, then see which "words" are closest
to Generator Gawl's embedding.
"""

### For loop to make sentences
# userlist = list(data['username'].drop_duplicates())

# sentences = []
# for user in tqdm(userlist, total=len(userlist)):
#     sentences.append(list(data[data['username'] == user]\
#         .sort_values(by='my_last_updated')['anime_id']))

# group_by_user = data.groupby('username')
# sentences = []
# for _, user_group in tqdm(group_by_user, total=len(group_by_user)):
#     sentences.append(list(user_group\
#         .sort_values(by='my_last_updated')['anime_id']))


sentences = []
for chunk in tqdm(pd.read_csv(filepath,
                    chunksize=10000000,
                    usecols=['username', 'my_last_updated', 'anime_id'])):
    group_by_user = chunk.groupby('username')
    for _, user_group in tqdm(group_by_user, total=len(group_by_user)):
        # sentences.append(list(user_group\
        #     .sort_values(by='my_last_updated')['anime_id']))
        sentences.append([str(x) for x in list(user_group\
            .sort_values(by='my_last_updated')['anime_id'])])

# pickle.dump(sentences,
#             open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\word2vec_sentences.pkl", 'wb'))












