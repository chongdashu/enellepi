import google_query
import pickle
import time
import pprint
import random
import math

import concordance
import naivebayes
import semantic_orientation
import freqdist

random.seed(6863)

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def get_list_from_dictionary(dict):
	list = []
	for (key,value) in dict.iteritems():
		list.append(value)
	return list

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

data_free = pickle.load(open('data/dataset_free.dat'))
random.shuffle(data_free)

data_paid = pickle.load(open('data/dataset_paid.dat'))
random.shuffle(data_paid)

'''
Create lists of the data, so that it's easier to iterate subsets of them.
'''
dataset_free = get_list_from_dictionary(data_free)
dataset_paid = get_list_from_dictionary(data_paid)

def analyze(datapoint):

	info = datapoint['info']
	phrases = datapoint['phrases']

	text_classification = naivebayes.classify_text(info['text'])
	title_classification = naivebayes.classify_text(info['title'])
	# so = semantic_orientation.calculate_overall_so_dist(phrases)
	so = freqdist.calculate_average_so(phrases)

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

def get_star_rating(a_entry):
	text_polarity = a_entry['text_classification']
	title_polarity = a_entry['title_classification']
	so = a_entry['semantic_orientation']
	
	if so == 0.0:
		return 3.0
	
	if text_polarity == 'pos':
		if so < 0.10:
			return 3.0
		elif so < 0.25:
			if title_polarity == 'pos':
				return 5.0
			else:
				return 4.0
		else:
			return 5.0
	if text_polarity == 'neg':
		if so > -0.25:
			return 2.0
		else:
			return 1.0

def analyze_all(datasetType):
	results = []
	
	dataset = []
	if datasetType == "free":
		dataset = dataset_free
	elif datasetType == "paid":
		dataset = dataset_paid

	for datapoint in dataset:

		original_index = datapoint['original_index']
		
		info = datapoint['info']
		phrases = datapoint['phrases']
		
		text = info['text']
		title = info['title']
		rating = info['rating']

		a = analyze(datapoint)
		rating_calculated = get_star_rating(a)
		
		results.append({"original_index": original_index,
			"text" : text,
			"title" : title,
			"text-cls" : a['text_classification'],
			"title-cls" : a['title_classification'],
			'so' : a['semantic_orientation'],
			'phrases' : phrases,
			'rating-user' : rating,
			'rating-calculated': rating_calculated
			});

	return results

def analyze_all_free():
	return analyze_all("free")

def analyze_all_paid():
	return analyze_all("paid")
