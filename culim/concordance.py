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
#text.concordance("excellent")
#index = text._concordance_index
index = ConcordanceIndex(text.tokens, key=lambda s:s.lower())
excellist = index.offsets("excellent");
poorlist = index.offsets("poor");

negative = ["poor", "bad", "unlikeabl", "unfun" "aweful", "terribl", "crap"];
positive = ["excellent", "good", "fun", "nice", "cool", "awesome" ];

def OrientationDist(word1, word2, ispositive):
	wb = [];
	if ( ispositive == True): wb = positive;
	else: wb = negative;
	totaldist = 0;
	totalcount = 0;

	w1l = index.offsets( word1 );
	for w1 in w1l:
		for i in range(1, 50):
			for j in range(1, 50):
				if ( i == j ): continue;
				if ( w1 + j >= len(text.tokens) ): continue;
				if ( w1 + i >= len(text.tokens) ): continue;
				if ( w1 - j < 0 ): continue;
				for  w in wb :
					if (( text.tokens[w1+i] == word2 and text.tokens[w1+j] == w[:len(text.tokens[w1+j])] ) or
					( text.tokens[w1+i] == word2 and text.tokens[w1-j] == w[:len(text.tokens[w1-j])])):
						totalcount += 1;
						totaldist += abs(j) + i;
	if ( totalcount > 0 ):
		rv = (1.0 * totaldist) / totalcount;
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

