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

def get_min_and_max_logratios(data):
	f = open('data/pmi_distance_free_50.dat')
	so_dist_free = pickle.load(f)
	f.close()

	log_ratios = []
	for i in so_dist_free:
		log_ratio = 0.0
		for so_info in so_dist_free[i]:
			log_ratio = log_ratio + so_info['log_ratio']
		if len(so_dist_free[i]) > 0:
			log_ratio = log_ratio / len(so_dist_free[i])
		log_ratios.append(log_ratio)

	return (min(log_ratios), max(log_ratios))

analysis = {}
















