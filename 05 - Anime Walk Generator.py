# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 06:50:26 2021

@author: Connor
"""

import copy

class anime_walk():
    def __init__(self, starting_anime_id, max_iter, n_closest=5):
        self.max_iter = max_iter
    
def next_anime(anime_walk, n_closest=5):
    # Make a deepcopy of anime_walk
    anime_walk = copy.deepcopy(anime_walk)
    
    # Get last element of walk
    anime_id = anime_walk[-1]
    
    # Get n most similar anime
    most_similar_anime = model.wv.most_similar(positive=[str(anime_id)], topn=n_closest)
    # Filter to only unwatched series
    most_similar_anime = [x for x in most_similar_anime if x[0] not in anime_walk]
    
    # Check that most_similar_anime is not empty
    if most_similar_anime:
        # Made the next random choice
        p = np.array([x[1] for x in most_similar_anime])
        p /= sum(p)
        a = [x[0] for x in most_similar_anime]
        random_choice = np.random.choice(a, p=p)
    
        # Manage walk
        anime_walk.append(random_choice)
    return anime_walk

def make_anime_walk(start_anime_id, max_iter=1000, n_closest=5):
    anime_walk = [str(start_anime_id)]
    for ind in range(max_iter):
        check_len = len(anime_walk)
        anime_walk = next_anime(anime_walk, n_closest=n_closest)
        # No new anime to add
        if len(anime_walk) == check_len:
            break
    
    return anime_walk

# Starting from Neon Genesis Evangelion '30'
anime_walk_length = []
for ind in tqdm(range(1000), total=1000):
    anime_walk_length.append(len(make_anime_walk(30, n_closest=10)))
# Visualize anime walk lengths in a histogram
pd.Series(anime_walk_length).hist()












