from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

import enellepi
import pickle

file = open("topfree.dat", 'r')
free_reviews = pickle.load(file)
file.close()

file = open("toppaid.dat", 'r')
paid_reviews = pickle.load(file)
file.close()

test_review = paid_reviews[0]['text']
test_review_tokenized = word_tokenize(test_review)
test_review_pos = pos_tag(test_review_tokenized);


