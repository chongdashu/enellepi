import google_query
import pickle
import time
import pprint
import random
import math

original_free_dataset = pickle.load(open('data/topfree.dat'))
original_paid_dataset = pickle.load(open('data/toppaid.dat'))

original_free_phrases = pickle.load(open('data/phrases_2word_free.dat'))
original_paid_phrases = pickle.load(open('data/phrases_2word_paid.dat'))

output_free = {}
output_paid = {}

for i in range(len(original_free_dataset)):

	index = i
	info = original_free_dataset[i]
	phrases = original_free_phrases[i]

	data = { "original_index" : i, "info:" : info, "phrases" : phrases}
	output_free[i] = data

for i in range(len(original_paid_dataset)):

	index = i
	info = original_paid_dataset[i]
	phrases = original_paid_phrases[i]

	data = { "original_index" : i, "info:" : info, "phrases" : phrases}
	output_paid[i] = data

pickle.dump(output_free, open('data/dataset_free.dat', 'w'))
pickle.dump(output_paid, open('data/dataset_paid.dat', 'w'))


