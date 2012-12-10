import google_query
import pickle
import time
import pprint
import random
import math

import concordance
import naivebayes
import semantic_orientation

random.seed(6.863)

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

data_free = pickle.load(open('dataset_free.dat'))
random.shuffle(data_free)

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

def analyze(datapoint):

	info = datapoint['info']
	phrases = datapoint['phrases']

	text_classification = naivebayes.classify_text(info['text'])
	title_classification = naivebayes.classify_text(info['title'])
	so = semantic_orientation.calculate_overall_so_dist(phrases)

	res = { "text_classification" : text_classification, 
			"title_classification" : title_classification, 
			"semantic_orientation" : so }

	return res







