import google_query
import pickle
import time
import pprint
import random
import math
import nltk
import re

from nltk.corpus import movie_reviews
from nltk.text import ConcordanceIndex

text = nltk.Text(movie_reviews.words())
index = ConcordanceIndex(text.tokens, key=lambda s:s.lower())

#text.concordance("excellent")
#index = text._concordance_index

excellist = index.offsets("excellent")
poorlist = index.offsets("poor")

negative = ["poor", "bad", "unlikeabl", "unfun" "awful", "terribl", "crap", "frustrat", "horribl"];
positive = ["excellent", "good", "fun", "nice", "cool", "awesome", "addict", "great" ];

def OrientationDist(word1, word2, ispositive):
	wb = []
	if ispositive: 
		wb = positive
	else: 
		wb = negative
	
	totaldist = 0
	totalcount = 0

	# Iterate over all words in the movie reviews corpus and all the words in the 'wb' list,
	# which is either the list 'positive' or 'negative', and increment 'appcount' if any words
	# in the movie review corpus are in 'wb'
	#
	# Question: Is the above behavior what we actually want here?
	#		If yes, this seems like a calculation we should do once for the positive list and
	#       once for the negative list. We could just reuse these values as necessary.
	appcount = 0
	for w in text.tokens:
		for wk in wb:
			if wk == w[:len(wk)]: 
				appcount += 1

	# Obtain the first 20 offsets for 'word1' in the movie review corpus.
	w1l = index.offsets( word1 )[:20]; # take the first 20 offsets only, to save time.
	
	# Iterate over all 20 offsets. For each offset iterate over a 19x19 grid of values
	# starting at point (1, 1) and ending at (20, 20)
	#
	# Question: Is j supposed to iterate over negative values? (i.e. is j supposed to
	#           iterate over the range 'reversed(range(-19, 0))'?) I ask because the
	#		    absolute value of j is used to compute 'totaldist' below.
	for w1 in w1l:
		for i in range(1, 20):
			for j in range(1, 20):

				if i == j: 
					continue
				if (w1 + j) >= len(text.tokens): 
					continue
				if (w1 + i) >= len(text.tokens): 
					continue
				if (w1 - j) < 0: 
					continue
				
				# Iterate over all words in 'wb' (this is either the list 'negative' or 'positive')	
				for w in wb:
					# print "word1:%s word2:%s w1:%s i:%s j:%s w:%s" % (word1, word2, w1, i, j, w)
					# print "cur_iword=%s, cur_jword=%s, cur_j-word=%s, pol_word=%s" % (text.tokens[w1+i], text.tokens[w1+j][:len(w)], text.tokens[w1-j][:len(w)], w)
					
					# The condition for increasing 'totalcount' and 'totaldist' are as follows based on
					# what was written below:
					#	1. 'word2' is 'i' words from 'word1' and a word in 'wb' is 'j' words from 'word1'
					#   2. 'word2' is 'i' words from 'word1' and a word in 'wb' is '-j' words from 'word1'
					if (( text.tokens[w1+i] == word2 and text.tokens[w1+j][:len(w)] == w ) or ( text.tokens[w1+i] == word2 and text.tokens[w1-j][:len(w)] == w)):
						totalcount += 1;
						totaldist += abs(j) + i;
						
	if totalcount > 0:
		rv = (1.0 * totaldist) / totalcount / appcount;
	else:
		rv = 100;
		
	return rv;
	
	

def OrientationBayes(word1, word2, key):
	keylist = index.offsets(key);
	esl = [key];
	w1l = [word1];
	w2l = [word2];

	excellmatchcount = 0;
	excellcount = 0;
	for k in esl:
		kl = index.offsets(k);
		excellcount += len(kl);
		for idx in kl:
			for i in range(-20, 20):
				for j in range(i, i+5):
					for w1 in w1l:
						for w2 in w2l:
							if ( text.tokens[idx+i] == w1 and text.tokens[idx+j] == w2 ):
								excellmatchcount += 1;
	excellprob = 1.0 * excellmatchcount / excellcount;
	print excellmatchcount, excellcount;
	
	return excellprob;

def example1():
	#rv = OrientationBayes("extremely", "annoying", "excellent");
	rv = OrientationDist("extremely", "annoying", True);
	rv2 = OrientationDist("extremely", "annoying", False);

	#text.concordance("annoying")
	#index.offsets('annoying')
	#sentences = movie_reviews.sents()

