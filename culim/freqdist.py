import nltk
import math
import pprint
from nltk.corpus import movie_reviews

mix_words = movie_reviews.words()
pos_words = movie_reviews.words(categories="pos")
neg_words = movie_reviews.words(categories="neg")

mix_freqd = nltk.FreqDist([w.lower() for w in mix_words])
pos_freqd = nltk.FreqDist([w.lower() for w in pos_words])
neg_freqd = nltk.FreqDist([w.lower() for w in neg_words])

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def so(word):
	return math.log((pos_freqd.freq(word)+1E-9)/(neg_freqd.freq(word)+1E-9))

def so_2(word1, word2):
	return so(word1) + so(word2)

def calculate_phrase_so(phrase):
	(word1, tag1) = phrase[0]
	(word2, tag2) = phrase[1]

	word1 = replace_contractions(word1)
	word2 = replace_contractions(word2)

	return so_2(word1, word2)

def calculate_average_so(phrases):
	if len(phrases) == 0:
		return 0.0

	so = 0.0;
	for phrase in phrases:
		so = so + calculate_phrase_so(phrase)

	return so/len(phrases)

# pos_freqd.freq("annoying")
# neg_freqd.freq("annoying")