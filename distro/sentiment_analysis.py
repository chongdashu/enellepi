import simplejson as json
import urllib
import httplib
import requests
import pickle
import time
import pprint
import random
import math

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

'''
Seed the randomizer.
'''
random.seed(time.clock())

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

'''
Get all the reviews for the top free apps.
'reviews' is a dictionary, where:
	key: review-index
	value: array of phrases extracted from that review.
'''
data_free = pickle.load(open('topfree.dat'))
phrases_free = pickle.load(open('phrases_2word_free.dat'));

data_paid = pickle.load(open('toppaid.dat'))
phrases_paid = pickle.load(open('phrases_2word_paid.dat'));

def get_sentiment(phrase):
	payload = {'text': phrase}
	r = requests.post("http://text-processing.com/api/sentiment/", data=payload)
	return json.loads(r.text)

def get_free_sentiments():
	all_sentiments = {}
	for i in range(10):
		all_sentiments[i] = []

		phrases = phrases_free[i]
		for phrase in phrases:
			(word1, tag1) = phrase[0]
			(word2, tag2) = phrase[1]

			word1 = replace_contractions(word1)
			word2 = replace_contractions(word2)

			query = word1 + " " + word2
			sentiment = get_sentiment(query)

			all_sentiments[i].append({ "phrase" : phrase, "sentiment" : sentiment})

	free_sentiments = all_sentiments
	return all_sentiments
