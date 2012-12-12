import google_query
import pickle
import time
import pprint
import random
import math
import nltk

from nltk.classify.svm import SvmClassifier
from nltk.classify import NaiveBayesClassifier
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def review_features(datapoint):
	'''
	Feature vector for use with Naive Bayes.
	'''
	return { "text-cls" : datapoint["text-cls"], 
	"title-cls" : datapoint["title-cls"],
	"so" : datapoint["so"]}

def sci_features(datapoint):
	'''
	Feature vector for use with SVMs.
	'''
	txt_cls = 0.0
	if datapoint["text-cls"] == "pos":
		txt_cls = 1.0
	else:
		txt_cls = -1.0

	title_cls = 0.0
	if datapoint["title-cls"] == "pos":
		title_cls = 1.0
	else:
		title_cls = -1.0

	return [datapoint["so"]]

def svm_classify(datapoints):
	datafeats = [sci_features(datapoint) for datapoint in datapoints]
	datalabels = [datapoint["rating-user"] for datapoint in datapoints]

	classifier = svm.LinearSVC()
	# classifier.fit(datafeats, datalabels)
	scores = cross_validation.cross_val_score(classifier, datafeats, datalabels, cv=5)
	print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() / 2)


results_free = pickle.load(open('results/results_free.dat'))
results_paid = pickle.load(open('results/results_paid.dat'))


### SVM classifier
STAR_RATING_POSITIVE_THRESHOLD_VALUE = 3.0

results_free_pos = [datapoint for datapoint in results_free if datapoint['rating-user'] >= STAR_RATING_POSITIVE_THRESHOLD_VALUE]
results_free_neg = [datapoint for datapoint in results_free if datapoint['rating-user'] < STAR_RATING_POSITIVE_THRESHOLD_VALUE]

results_paid_pos = [datapoint for datapoint in results_paid if datapoint['rating-user'] >= STAR_RATING_POSITIVE_THRESHOLD_VALUE]
results_paid_neg = [datapoint for datapoint in results_paid if datapoint['rating-user'] < STAR_RATING_POSITIVE_THRESHOLD_VALUE]

print \
'Analyzing free apps:'
print '-----------------------------------------'
print \
"Assuming we correctly classify the the positive reviews, \
if we use semantic-orientation to calculate the exact star rating, we get the following results:"
svm_classify(results_free_pos)

print '-----------------------------------------'

print \
"Assuming we correctly classify the the negative reviews, \
if we use semantic-orientation to calculate the exact star rating, we get the following results:"
svm_classify(results_free_neg)

print \
'Analyzing paid apps:'
print '-----------------------------------------'
print \
"Assuming we correctly classify the the positive reviews, \
if we use semantic-orientation to calculate the exact star rating, we get the following results:"
svm_classify(results_paid_pos)

print '-----------------------------------------'

print \
"Assuming we correctly classify the the negative reviews, \
if we use semantic-orientation to calculate the exact star rating, we get the following results:"
svm_classify(results_paid_neg)

#results_free_pos = [datapoint for datapoint in results_free if datapoint['text-cls'] == "pos"]
#results_free_neg = [datapoint for datapoint in results_free if datapoint['text-cls'] == "neg"]



'''
# Naive Bayes classifier
datafeats2 = [(review_features(datapoint), datapoint['rating-user']) for datapoint in results_free]
cutoff = len(datafeats2)*3/4
 
trainfeats = datafeats2[:cutoff]
testfeats = datafeats2[cutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
'''


#datafeats = [(review_features(datapoint), str(datapoint['rating-user'])) for datapoint in results_free]
#classifier = SvmClassifier.train(datafeats)

