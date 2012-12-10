import pickle
import time
import pprint
import random
import math
import concordance
import nltk.classify.util

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize, WhitespaceTokenizer

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

def word_feats(words):
	''' 
	Converts a list of words into a bag of words dictionary. 
	'''
	return dict([(word, True) for word in words])

'''
Train a classifier on 'positive' and 'negative' reviews from the movie_reviews corpus from NLTK.
This uses the 'bag-of-words' model.

Grab a review from our extracted Google Play dataset.
Classify the review using our trained classifier.
'''
data_free = pickle.load(open('topfree.dat'))
data_paid = pickle.load(open('toppaid.dat'))

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

trainfeats = posfeats + negfeats
classifier = NaiveBayesClassifier.train(trainfeats)


def example1():
	'''
	Credits:
	Streamhacker.com
	http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
	'''
	negids = movie_reviews.fileids('neg')
	posids = movie_reviews.fileids('pos')
	 
	negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
	posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
	 
	negcutoff = len(negfeats)*3/4
	poscutoff = len(posfeats)*3/4
	 
	trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
	testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
	print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
	 
	classifier = NaiveBayesClassifier.train(trainfeats)
	print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
	classifier.show_most_informative_features()

def classify_review(index = 10):
	'''
	Train a classifier on 'positive' and 'negative' reviews from the movie_reviews corpus from NLTK.
	This uses the 'bag-of-words' model.

	Grab a review from our extracted Google Play dataset.
	Classify the review using our trained classifier.
	'''

	sample_title = data_free[index]['title']
	sample_text = data_free[index]['text']

	sample_text_tokens = [replace_contractions(w).encode('ascii', 'ignore') for w in word_tokenize(sample_text)]
	sample_title_tokens = [replace_contractions(w).encode('ascii', 'ignore') for w in word_tokenize(sample_title)]

	text_features = word_feats(sample_text_tokens)
	title_features = word_feats(sample_title_tokens)

	text_label  = classifier.classify(text_features)
	title_label = classifier.classify(title_features)

	print 'Results of classification:'
	print 'Review #:%s\nTitle:%s\nText:%s\n' % (index, sample_title, sample_text)
	print '------------------------------'
	print 'Title classified as: %s\nText classified as: %s' %(title_label, text_label)

'''
Example:
classify_review(12)
'''








