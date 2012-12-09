#!/usr/bin/python

import sys
import pickle

def log_ratio_2_star_rating(log_ratio):
	if log_ratio < -3.0:
		return 1.0
	elif log_ratio < -0.75:
		return 2.0
	elif log_ratio < -0.25 or log_ratio == 0.0:
		return 3.0
	elif log_ratio < 2.0:
		return 4.0
	else:
		return 5.0
		
if __name__ == "__main__":
	results = pickle.load(open(sys.argv[1], 'r'))
	print "index", "\t", "star-rating"
	for i in range(len(results)):
		if len(results[i]) == 0:
			continue
		sum = 0
		for j in range(len(results[i])):
			sum = sum + log_ratio_2_star_rating(results[i][j]['log_ratio'])
		average = sum/len(results[i])
		print i, "\t", average