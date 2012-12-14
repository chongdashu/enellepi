#!/usr/bin/python

import sys
import pickle

if sys.argv[1] < 3:
	print "USAGE: ./make_pickle_from_sample.py sample_file1 sample_file2"

x = pickle.load(open('dataset_free.dat'))
y = pickle.load(open('dataset_free.dat'))

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')

f1_lines = f1.readlines()
f2_lines = f2.readlines()

f1_accurate = []
f1_inaccurate = []
f2_accurate = []
f2_inaccurate = []

accuracy_switch = True
for i in range(2, len(f1_lines)):

	f1_line = f1_lines[i].rstrip()
	if f1_line == '' or f1_line[:6] == 'rating' or f1_line[0] == '-':
		continue
	
	if f1_line == "INACCURATE":
		accuracy_switch = False
	if f1_line[0] == '[':
		f1_line = f1_line.split(' ')
		index = int(f1_line[1])
		if accuracy_switch:
			f1_accurate.append(index)
		else:
			f1_inaccurate.append(index)

f1_accurate_words = {}
for i in range(len(x)):
	if x[i]['original_index'] in f1_accurate:
		f1_accurate_words[ x[i]['original_index'] ] = x[i]
f1_inaccurate_words = {}
for i in range(len(x)):
	if x[i]['original_index'] in f1_inaccurate:
		f1_inaccurate_words[ x[i]['original_index'] ] = x[i]


pickle.dump(f1_accurate_words, open('dataset_accurate_free.dat', 'w'))
pickle.dump(f1_inaccurate_words, open('dataset_inaccurate_free.dat', 'w'))

accuracy_switch = True
for i in range(2, len(f2_lines)):

	f2_line = f2_lines[i].rstrip()
	if f2_line == '' or f2_line[:6] == 'rating' or f2_line[0] == '-':
		continue
	
	if f2_line == "INACCURATE":
		accuracy_switch = False	
	if f2_line[0] == '[':
		f2_line = f2_line.split(' ')
		index = int(f2_line[1])
		if accuracy_switch:
			f2_accurate.append(i)
		else:
			f2_inaccurate.append(i)
			
f2_accurate_words = {}
for i in range(len(x)):
	if x[i]['original_index'] in f2_accurate:
		f1_accurate_words[ x[i]['original_index'] ] = x[i]
f2_inaccurate_words = {}
for i in range(len(x)):
	if x[i]['original_index'] in f2_inaccurate:
		f2_inaccurate_words[ x[i]['original_index'] ] = x[i]

pickle.dump(f2_accurate_words, open('dataset_accurate_paid.dat', 'w'))
pickle.dump(f2_inaccurate_words, open('dataset_inaccurate_paid.dat', 'w'))
