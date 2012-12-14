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
from sklearn.metrics import confusion_matrix

import crossvalidation

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

results_free = pickle.load(open('results/results_free.dat'))
results_paid = pickle.load(open('results/results_paid.dat'))

results_accurate_free = pickle.load(open('results/results_accurate_free.dat'))
results_accurate_paid = pickle.load(open('results/results_accurate_paid.dat'))

classifier_free_pos = pickle.load(open('models/cls_free_pos.model'))
classifier_free_neg = pickle.load(open('models/cls_free_neg.model'))
classifier_paid_pos = pickle.load(open('models/cls_paid_pos.model'))
classifier_paid_neg = pickle.load(open('models/cls_paid_neg.model'))

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

	#return [datapoint["so"]]
	#return [txt_cls, datapoint["so"]]
	return [title_cls, txt_cls, datapoint["so"]]

def classify_review(review_data, datasetType):
	datapoint = {"text-cls" : review_data["text_classification"], "title-cls" : review_data["title_classification"], "so" : review_data["semantic_orientation"]}
	datapointfeats = sci_features(datapoint)
	
	classifier = {}

	if (datasetType == 'free'):
		if review_data["text_classification"] == "pos":
			classifier = classifier_free_pos
		else:
			classifier = classifier_free_neg
	else:
		if review_data["text_classification"] == "pos":
			classifier = classifier_paid_pos
		else:
			classifier = classifier_paid_neg

	label = classifier.predict(datapointfeats)

	return label[0]

def svm_classify(datapoints):
	datafeats = [sci_features(datapoint) for datapoint in datapoints]
	datalabels = [datapoint["rating-user"] for datapoint in datapoints]

	classifier = svm.SVC(C=1) # svm.LinearSVC also works.
	classifier.fit(datafeats, datalabels)
	scores = cross_validation.cross_val_score(classifier, datafeats, datalabels, cv=10)
	precision = cross_validation.cross_val_score(classifier, datafeats, datalabels, cv=10, score_func=metrics.precision_score)
	recall = cross_validation.cross_val_score(classifier, datafeats, datalabels, cv=10, score_func=metrics.recall_score)
	f1 = cross_validation.cross_val_score(classifier, datafeats, datalabels, cv=10, score_func=metrics.f1_score)
	
	classifier.fit(datafeats, datalabels)
	print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() / 2)
	print "Precision: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std() / 2)
	print "Recall: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std() / 2)
	print "F1-score: %0.2f (+/- %0.2f)" % (f1.mean(), f1.std() / 2)

	prediction = classifier.predict(datafeats)
	cm = confusion_matrix(datalabels, prediction)

	print cm

	return classifier

def svm_tune_parameters(datapoints):
	datafeats = [sci_features(datapoint) for datapoint in datapoints]
	datalabels = [datapoint["rating-user"] for datapoint in datapoints]

	crossvalidation.tune_parameters(datafeats, datalabels)

def get_sci_X_and_Y(datapoints):
	datafeats = [sci_features(datapoint) for datapoint in datapoints]
	datalabels = [datapoint["rating-user"] for datapoint in datapoints]

	return (datafeats, datalabels)

def save_classifier(classifier, filename):
	pickle.dump(classifier, open(filename))

def create_models():
	STAR_RATING_POSITIVE_THRESHOLD_VALUE = 3

	results_free_pos = [datapoint for datapoint in results_free if datapoint['rating-user'] >= STAR_RATING_POSITIVE_THRESHOLD_VALUE]
	results_free_neg = [datapoint for datapoint in results_free if datapoint['rating-user'] < STAR_RATING_POSITIVE_THRESHOLD_VALUE]

	results_paid_pos = [datapoint for datapoint in results_paid if datapoint['rating-user'] >= STAR_RATING_POSITIVE_THRESHOLD_VALUE]
	results_paid_neg = [datapoint for datapoint in results_paid if datapoint['rating-user'] < STAR_RATING_POSITIVE_THRESHOLD_VALUE]

	classifier_free_pos = svm_classify(results_free_pos)
	classifier_free_neg = svm_classify(results_free_neg)
	classifier_paid_pos = svm_classify(results_paid_pos)
	classifier_paid_neg = svm_classify(results_paid_neg)

	pickle.dump(classifier_free_pos, open('models/cls_free_pos.model', 'w'))
	pickle.dump(classifier_free_neg, open('models/cls_free_neg.model', 'w'))
	pickle.dump(classifier_paid_pos, open('models/cls_paid_pos.model', 'w'))
	pickle.dump(classifier_paid_neg, open('models/cls_paid_neg.model', 'w'))

def run():

	'''
	Unfiltered Datasets
	'''

	print ""
	print '========================================'
	print '	Datasets (Pre-sorted)'
	print '========================================'
	STAR_RATING_POSITIVE_THRESHOLD_VALUE = 3

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
	cls_free_pos = svm_classify(results_free_pos)

	print '-----------------------------------------'

	print \
	"Assuming we correctly classify the the negative reviews, \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	cls_free_neg = svm_classify(results_free_neg)

	print ""

	print \
	'Analyzing paid apps:'
	print '-----------------------------------------'
	print \
	"Assuming we correctly classify the the positive reviews, \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	cls_paid_pos = svm_classify(results_paid_pos)

	print '-----------------------------------------'

	print \
	"Assuming we correctly classify the the negative reviews, \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	cls_paid_neg = svm_classify(results_paid_neg)

	print ""

	results_combined_pos = results_free_pos + results_paid_pos
	results_combined_neg = results_free_neg + results_paid_neg

	print \
	'Analyzing combined:'
	print '-----------------------------------------'
	print \
	"Assuming we correctly classify the the positive reviews, \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	svm_classify(results_combined_pos)

	print '-----------------------------------------'

	print \
	"Assuming we correctly classify the the negative reviews, \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	svm_classify(results_combined_neg)

	print ""
	print '========================================'
	print '	Datasets (Unsorted)'
	print '========================================'


	print \
	'Analyzing free apps:'
	print '-----------------------------------------'
	print \
	"Assuming we do not pre-sort the free apps \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	svm_classify(results_free)

	print '-----------------------------------------'

	print \
	'Analyzing free apps:'
	print '-----------------------------------------'
	print \
	"Assuming we do not pre-sort the paid apps \
	if we use semantic-orientation to calculate the exact star rating, we get the following results:"
	svm_classify(results_paid)

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


