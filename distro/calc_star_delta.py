#!/usr/bin/python

import sys
import pickle
import math

#get lograt2star results
result_file = open(sys.argv[1], 'r')
result_lines = result_file.readlines()
result_lines = result_lines[1:]
for i in range(len(result_lines)):
	result_lines[i] = result_lines[i].strip().split(" \t")
	result_lines[i][0] = int(result_lines[i][0])
	result_lines[i][1] = float(result_lines[i][1])
data = pickle.load(open(sys.argv[2]))

def get_precision():
	p_sum = 0
	for i in range(len(result_lines)):
		entry = data[result_lines[i][0]]
		if math.fabs(entry['rating'] - result_lines[i][1]) < 0.01:
			p_sum = p_sum + 1
	return (p_sum * 1.0) / len(result_lines)

if __name__ == "__main__":
	print "precision =", get_precision()
	print "index", "\t", "old *-val", "\t", "new *-val", "\t", "delta"
	for i in range(len(result_lines)):
		entry = data[result_lines[i][0]]
		delta_val = entry['rating'] - result_lines[i][1]
		print result_lines[i][0], "\t", entry['rating'], "\t", result_lines[i][1], "\t", delta_val
