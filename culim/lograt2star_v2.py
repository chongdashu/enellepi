#!/usr/bin/python
#In this version of the script, we average the log ratios instead of the star-ratings.

import sys
import pickle
import math

def round_2_nearest_half(num):
	if num == 0.0 or num == 0.5 or num == 1.0 or num == 1.5 or num == 2.0 or num == 2.5 or num == 3.0 or num == 3.5 or num == 4.0 or num == 4.5 or num == 5.0:
		return num
		
	if num < 0.5:
		temp1 = 0.5 - num
		if(temp1 <= num):
			return 0.5
		else:
			return 0.0
	elif num < 1.0:
		temp1 = 1.0 - num
		temp2 = num - 0.5
		if(temp1 <= temp2):
			return 1.0
		else:
			return 0.5
	elif num < 1.5:
		temp1 = 1.5 - num
		temp2 = num - 1.0
		if(temp1 <= temp2):
			return 1.5
		else:
			return 1.0
	elif num < 2.0:
		temp1 = 2.0 - num
		temp2 = num - 1.5
		if(temp1 <= temp2):
			return 2.0
		else:
			return 1.5
	elif num < 2.5:
		temp1 = 2.5 - num
		temp2 = num - 2.0
		if(temp1 <= temp2):
			return 2.5
		else:
			return 2.0
	elif num < 3.0:
		temp1 = 3.0 - num
		temp2 = num - 2.5
		if(temp1 <= temp2):
			return 3.0
		else:
			return 2.5
	elif num < 3.5:
		temp1 = 3.5 - num
		temp2 = num - 3.0
		if(temp1 <= temp2):
			return 3.5
		else:
			return 3.0
	elif num < 4.0:
		temp1 = 4.0 - num
		temp2 = num - 3.5
		if(temp1 <= temp2):
			return 4.0
		else:
			return 3.5
	elif num < 4.5:
		temp1 = 4.5 - num
		temp2 = num - 4.0
		if(temp1 <= temp2):
			return 4.5
		else:
			return 4.0
	else:
		temp1 = 5.0 - num
		temp2 = num - 4.5
		if(temp1 <= temp2):
			return 5.0
		else:
			return 4.5

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
			sum = sum + results[i][j]['log_ratio']
		average = sum/len(results[i])
		ex_average = round_2_nearest_half(log_ratio_2_star_rating(average))
		print i, "\t", ex_average