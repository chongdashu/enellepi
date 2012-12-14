#!/usr/bin/python

import sys
import pickle

if sys.argv[1] < 3:
	print "USAGE: ./make_pickle_from_sample.py sample_file1 sample_file2"
	
f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')

f1_lines = f1.readlines()
f2_lines = f2.readlines()

f1_accurate = {'1.0' : [], '2.0' : [], '3.0' : [], '4.0' : [], '5.0' : []}
f2_accurate = {'1.0' : [], '2.0' : [], '3.0' : [], '4.0' : [], '5.0' : []}
f1_inaccurate = {'1.0' : [], '2.0' : [], '3.0' : [], '4.0' : [], '5.0' : []}
f2_inaccurate = {'1.0' : [], '2.0' : [], '3.0' : [], '4.0' : [], '5.0' : []}

accuracy_switch = True
cur_star_rating = 0.0
cur_entry = {'index' : 0, 'text': '', 'title' : ''}
for i in range(2, len(f1_lines)):

	f1_line = f1_lines[i].rstrip()
	if f1_line == '' or f1_line[:6] == 'rating' or f1_line[0] == '-':
		continue
		
	if f1_line[0] == '~':
		cur_star_rating = f1_line[2:5]
	if f1_line[0] == '[':
		f1_line = f1_line.split(' ')
		cur_entry['index'] = int(f1_line[1])
		
	if f1_line == "INACCURATE":
		accuracy_switch = False
	if f1_line[:4] == "text":
		cur_entry['text'] = f1_line.split(' ', 2)[2]
	if f1_line[:5] == "title":
		cur_entry['title'] = f1_line.split(' ', 2)[2]
		if accuracy_switch:
			f1_accurate[cur_star_rating].append(cur_entry)
			cur_entry = {'index' : 0, 'text': '', 'title' : ''}
		else:
			f1_inaccurate[cur_star_rating].append(cur_entry)
			cur_entry = {'index' : 0, 'text': '', 'title' : ''}

pickle.dump(f1_accurate, open('dataset_accurate_free.dat', 'w'))
pickle.dump(f1_inaccurate, open('dataset_inaccurate_free.dat', 'w'))

accuracy_switch = True
cur_star_rating = 0.0
for i in range(2, len(f2_lines)):

	f2_line = f2_lines[i].rstrip()
	if f2_line == '' or f2_line[:6] == 'rating' or f2_line[0] == '-':
		continue
		
	if f2_line[0] == '~':
		cur_star_rating = f2_line[2:5]
	if f2_line[0] == '[':
		f2_line = f2_line.split(' ')
		cur_entry['index'] = int(f2_line[1])
		
	if f2_line == "INACCURATE":
		accuracy_switch = False
	if f2_line[:4] == "text":
		cur_entry['text'] = f2_line.split(' ', 2)[2]
	if f2_line[:5] == "title":
		cur_entry['title'] = f2_line.split(' ', 2)[2]
		if accuracy_switch:
			f2_accurate[cur_star_rating].append(cur_entry)
			cur_entry = {'index' : 0, 'text': '', 'title' : ''}
		else:
			f2_inaccurate[cur_star_rating].append(cur_entry)
			cur_entry = {'index' : 0, 'text': '', 'title' : ''}

pickle.dump(f2_accurate, open('dataset_accurate_paid.dat', 'w'))
pickle.dump(f2_inaccurate, open('dataset_inaccurate_paid.dat', 'w'))
