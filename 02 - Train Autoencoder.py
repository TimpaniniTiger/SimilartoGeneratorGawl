# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:38:45 2021

@author: Connor
"""


import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from scipy.linalg import norm


data_dict = pickle.load( open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\ratings_matrix.pkl", 'rb') )

# user_index = data_dict['user_index']
anime_index = data_dict['anime_index']
ratings_matrix = data_dict['ratings_matrix']
del data_dict


### Autoencoder Model
ratings_matrix_input = keras.Input(shape=(14478), name="ratings_matrix_input")
# Embedding Layer
embedding = layers.Dense(5, activation="selu")(ratings_matrix_input)
x = layers.Dense(32, activation="selu")(embedding)
x = layers.BatchNormalization()(x)
x = layers.Dense(16, activation="selu")(x)
x = layers.BatchNormalization()(x)
# Autoencoder Layer
x = layers.Dense(5, activation="selu")(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(16, activation="selu")(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(32, activation="selu")(x)
x = layers.BatchNormalization()(x)
outputs = layers.Dense(14478, activation="selu")(x)

model = keras.Model(inputs=ratings_matrix_input, outputs=outputs, name="ratings_autoencoder")
model.compile(optimizer="Adam", loss="mse")

model.fit(ratings_matrix, ratings_matrix, epochs=5, batch_size=10000)


embedding_weights = model.layers[1].get_weights()[0]

### Extract Generator Gawl's weights
data_anime = pd.read_csv("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\AnimeList.csv")
# Find Generator Gawl
temp1 = data_anime[data_anime['title'].str.contains('Generator')]
# anime_id = 1022
gawl_weights = embedding_weights[anime_index[1022], :]

def get_n_closest(n_closest=5):
    n_closest += 1  # To account for the fact that Generator Gawl will be in the list
    # np.argmin(norm(embedding_weights - gawl_weights, axis=1))  # Diagnostic, of course the answer is Generator Gawl
    closest_anime = np.argpartition(norm(embedding_weights - gawl_weights, axis=1), n_closest)[:n_closest]
    
    anime_index_rev = {y: x for x, y in anime_index.items()}
    closest_anime_index = [anime_index_rev[x] for x in closest_anime]
    
    closest_anime_df = data_anime[data_anime['anime_id'].isin(closest_anime_index)]
    
    return closest_anime_df

temp3 = get_n_closest(100)
# temp2.to_csv("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\naive_5_closest.csv", index=False)
# temp3.to_csv("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\5_epochs_100_closest.csv", index=False)
# pickle.dump(embedding_weights,
#             open("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\5_epochs_embedding_weights.pkl", 'wb'))