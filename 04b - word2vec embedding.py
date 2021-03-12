# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:49:31 2021

@author: Connor
"""


import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from tqdm import tqdm
import pickle
from gensim.models.word2vec import Word2Vec


# sentences = pickle.load(open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\word2vec_sentences.pkl", 'rb'))

# class sentences_iterable():
#     def __init__(self, sentences):
#         self.sentences = sentences
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.sentences:
#             output = self.sentences.pop()
#             output = [str(x) for x in output]
#             return output
#         else:
#             StopIteration

class sentences_iterable(object):
    def __iter__(self):
        for sentence in pickle.load(open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\word2vec_sentences.pkl", 'rb')):
            yield [str(x) for x in sentence]
    

iterable = sentences_iterable()

model =\
Word2Vec(
    sentences=iterable,
    size=128,
    workers=4,
    iter=10)

# model.save("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\word2vec_model.model")

# Find most similar to Generator Gawl 
data_anime = pd.read_csv("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\AnimeList.csv")
# Find Generator Gawl
temp1 = data_anime[data_anime['title'].str.contains('Generator')]

model.wv.most_similar(positive=['1022'], topn=10)

def get_n_closest(n_closest, anime_id=1022):
    anime_id_list = model.wv.most_similar(positive=[str(anime_id)], topn=n_closest)
    print(anime_id_list)
    anime_id_list = [int(x[0]) for x in anime_id_list]
    return data_anime[data_anime['anime_id'].isin(anime_id_list)]

temp2 = get_n_closest(3)

# Neon Genesis Evangelion '30'
temp3 = get_n_closest(10, anime_id=30)

# Mobile Suit Gundam '80'
temp4 = get_n_closest(10, anime_id=80)

# Zeta Gundam
temp4 = get_n_closest(10, anime_id=85)


# Gundam X '92'
temp5 = get_n_closest(10, anime_id=92)

# Toward the Terra '2158'
temp5 = get_n_closest(10, anime_id=2158)

# Crest of the Stars
temp5 = get_n_closest(10, anime_id=290)
