#!/usr/bin/python

import pickle
import sys

if len(sys.argv) < 2:
	print 'usage: python <results dat file>'
	print 'example: python results_free.dat'
	sys.exit(0)

#load results
x = pickle.load(open(sys.argv[1]))

#iterate over all results
num_correct_tex_pols = 0
num_correct_tit_pols = 0
num_correct_two_pols = 0
num_correct_so_pols = 0
for i in range(len(x)):
	user_rating = float(x[i]['rating-user'])
	title_cls = x[i]['title-cls']
	text_cls = x[i]['text-cls']
	so = x[i]['so']
	
	#determine the accuracy of predicting a review's polarity based on the title
	if user_rating > 2.9 and title_cls == 'pos':
		num_correct_tit_pols += 1
	if user_rating < 2.9 and title_cls == 'neg':
		num_correct_tit_pols += 1
	
	#determine the accuracy of predicting a review's polarity based on the text
	if user_rating > 2.9 and text_cls == 'pos':
		num_correct_tex_pols += 1
	if user_rating < 2.9 and text_cls == 'neg':
		num_correct_tex_pols += 1
		
	#determine how much the above accuracies overlap
	if user_rating > 2.9 and title_cls == 'pos' and text_cls == 'pos':
		num_correct_two_pols += 1
	if user_rating < 2.9 and title_cls == 'neg' and text_cls == 'neg':
		num_correct_two_pols += 1
		
	#determine polarity's accuracy with respect to the so
	if so >= 0 and title_cls == 'pos':
		num_correct_so_pols += 1
	if so < 0 and title_cls == 'neg':
		num_correct_so_pols += 1

print "Polarity Accuracy of Titles :", (num_correct_tit_pols * 1.0) / len(x)
print "Polarity Accuracy of Text   :", (num_correct_tex_pols * 1.0) / len(x)
print ""
print "Overlap of Above Polarities :", (num_correct_two_pols * 1.0) / len(x) 
print ""
print "Polarity Accuracy wrt SO    :", (num_correct_so_pols * 1.0) / len(x) 