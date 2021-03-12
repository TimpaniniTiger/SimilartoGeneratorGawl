# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:26:07 2021

@author: Connor
"""


from gensim.utils import SaveLoad

model = SaveLoad("C:\\Users\\Connor\\Downloads\\UserAnimeList.csv\\word2vec_model.model")

def get_n_closest(anime_id, neg_anime_id=[], n_closest=60):
    anime_id_list = model.wv.most_similar(positive=[str(x) for x in anime_id], negative=[str(x) for x in neg_anime_id], topn=n_closest)
    similarity_scores = [x[1] for x in anime_id_list]
    print(anime_id_list)
    anime_id_list = [int(x[0]) for x in anime_id_list]
    temp_df = data_anime[data_anime['anime_id'].isin(anime_id_list)]
    old_cols = list(temp_df.columns)
    temp_df['similarity_score'] = similarity_scores
    temp_df = temp_df[['similarity_score'] + old_cols]
    return temp_df
    

# Mecha anime, apparently
anime_id = [
    30, 440, 218,
    153, 219, 441, 324, 80, 160, 400, 567, 820,
    2582, 95, 1288,
    930, 1095, 85, 1792, 96,
    89, 2254,
    2598, 290, 1459, 3079, 1542,
    3327, 878]
output = get_n_closest(anime_id)

# Inuyasha
anime_id = [
    249,
    210, 232, 552, 154, 530, 6, 516, 3588, 392, 189, 136,
    534, 1535, 61, 874, 1138,
    508, 1313,
    527, 379]
neg_anime_id = [
    269, 1816, 20,
    90, 225, 1221, 121, 246]
output = get_n_closest(anime_id, neg_anime_id=neg_anime_id)


# Ano Natu de Matteiru
anime_id = [1143, 566,
            1016, 3974, 1177, 650, 1022,
            917, 1180, 974, 870]
output = get_n_closest(anime_id)

anime_id = [11433,
            8917, 10721, 11597, 15379, 12883,
            9981, ]
output = get_n_closest(anime_id)