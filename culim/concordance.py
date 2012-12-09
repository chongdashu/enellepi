import google_query
import pickle
import time
import pprint
import random
import math
import nltk

from nltk.corpus import movie_reviews
text = nltk.Text(movie_reviews.words())
text.concordance("annoying")

index = text._concordance_index
index.offsets('annoying')

sentences = movie_reviews.sents()