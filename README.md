# SimilartoGeneratorGawl

Generator Gawl is semi-obscure 1998 scifi anime that I rather liked and I wondered if I could find an anime simialr to it.

A while back someone dumped the MyAnimeList Database to Kaggle (https://www.kaggle.com/azathoth42/myanimelist),
so I used that as my data source.

I had the most success by using gensim to train a Word2Vec embedding of a user's ratings
(i.e. order the ratings by time, then you get a "sentence" of rating "words", where each individual word is an anime_id),
which is contained in files 04 (makes the training data) and 04b (trains and uses the word2vec model). In particular
that embedding could accept a list of anime (both as positive and negative examples) and find the n most similar anime.

I also trained an autoencoder in 01 and 02, if you want to see how to use Tensorflow, but that embedding didn't work well.

Just in case you were curious, here's what it predicts are the 10 most similar anime:

anime_id, title
738	  Choujuu Densetsu Gestalt
1449	HeatGuy J
1558	Gilgamesh
2905	Geisters: Fractions of the Earth
3929	Ginsoukikou Ordian
6377	Gate Keepers 21
6962	Gasaraki
9922	Gakuen Senki Muryou
11441	Geneshaft
11950	Gad Guard
