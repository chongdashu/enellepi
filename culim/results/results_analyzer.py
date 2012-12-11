#!/usr/bin/python

import pickle
import sys

#Get command line arguments.
if len(sys.argv) < 2:
	print 'usage: python <results dat file>'
	print 'example: python results_free.dat'
	sys.exit(0)

POSITIVE_THRESHOLD = 2.4

#Load results from data file provided by user.
data = pickle.load(open(sys.argv[1]))
data100ofeach = []
pos_count = 0
neg_count = 0
for i in range(len(data)):
	user_rating = float(data[i]['rating-user'])
	if user_rating > POSITIVE_THRESHOLD and pos_count < 100:
		data100ofeach.append(data[i])
		pos_count += 1
	if user_rating < POSITIVE_THRESHOLD and neg_count < 100:
		data100ofeach.append(data[i])
		neg_count += 1

#Analyze the data on a per-rating basis
def analyze_all_by_rating():
	dist = get_rating_distribution()
	analysis_struct = {}
	
	#initialize analysis_struct
	dist_keys = dist.keys()
	for i in range(len(dist_keys)):
		analysis_struct[dist_keys[i]] = {'num_correct_tex_pols' : 0, 'num_correct_tit_pols' : 0, 'num_correct_two_pols' : 0, 'num_correct_so_pols' : 0}
	
	#fill up analysis_struct
	for i in range(len(data)):
		user_rating = float(data[i]['rating-user'])
		user_rating_s = data[i]['rating-user']
		
		title_cls = data[i]['title-cls']
		text_cls = data[i]['text-cls']
		so = data[i]['so']
		
		#determine the accuracy of predicting a review's polarity based on the title
		if user_rating > POSITIVE_THRESHOLD and title_cls == 'pos':
			analysis_struct[user_rating_s]['num_correct_tit_pols'] += 1
		if user_rating < POSITIVE_THRESHOLD and title_cls == 'neg':
			analysis_struct[user_rating_s]['num_correct_tit_pols'] += 1
		
		#determine the accuracy of predicting a review's polarity based on the text
		if user_rating > POSITIVE_THRESHOLD and text_cls == 'pos':
			analysis_struct[user_rating_s]['num_correct_tex_pols'] += 1
		if user_rating < POSITIVE_THRESHOLD and text_cls == 'neg':
			analysis_struct[user_rating_s]['num_correct_tex_pols'] += 1
		
		#determine how much the above accuracies overlap
		if user_rating > POSITIVE_THRESHOLD and title_cls == 'pos' and text_cls == 'pos':
			analysis_struct[user_rating_s]['num_correct_two_pols'] += 1
		if user_rating < POSITIVE_THRESHOLD and title_cls == 'neg' and text_cls == 'neg':
			analysis_struct[user_rating_s]['num_correct_two_pols'] += 1
		
		#determine polarity's accuracy with respect to the so
		if so >= 0 and title_cls == 'pos':
			analysis_struct[user_rating_s]['num_correct_so_pols'] += 1
		if so < 0 and title_cls == 'neg':
			analysis_struct[user_rating_s]['num_correct_so_pols'] += 1
	
	#print results
	print "\nBy-Rating Analysis"
	analysis_keys = analysis_struct.keys()
	for i in range(len(analysis_keys)):
		print "(",analysis_keys[i],")"
		print "# Correct Title      Polarizations: ", analysis_struct[analysis_keys[i]]['num_correct_tit_pols'], "\t", analysis_struct[analysis_keys[i]]['num_correct_tit_pols'] * 100.0 / dist[analysis_keys[i]], "%"
		print "# Correct Text       Polarizations: ", analysis_struct[analysis_keys[i]]['num_correct_tex_pols'], "\t", analysis_struct[analysis_keys[i]]['num_correct_tex_pols'] * 100.0 / dist[analysis_keys[i]], "%"
		print "# Correct Title/Text Polarizations: ", analysis_struct[analysis_keys[i]]['num_correct_two_pols'], "\t", analysis_struct[analysis_keys[i]]['num_correct_two_pols'] * 100.0 / dist[analysis_keys[i]], "%"
		print "# Correct w.r.t. SO  Polarizations: ", analysis_struct[analysis_keys[i]]['num_correct_so_pols'], "\t", analysis_struct[analysis_keys[i]]['num_correct_so_pols'] * 100.0 / dist[analysis_keys[i]], "%"
		print "\n"

#Obtains the distribution for the star-ratings in the provided data
def get_rating_distribution():
	dist = {}
	for i in range(len(data)):
		user_rating = float(data[i]['rating-user'])
		try:
			dist[user_rating] += 1
		except KeyError:
			dist[user_rating] = 0
	
	print "Rating Distribution"
	dist_keys = dist.keys()
	for i in range(len(dist_keys)):
		print dist_keys[i], "\t#=", dist[dist_keys[i]], "\t%=", dist[dist_keys[i]] * 100.0 / len(data)
	
	return dist

if __name__ == '__main__':
	analyze_all_by_rating()