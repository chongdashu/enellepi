#!/usr/bin/python
import pickle
import sys

x = pickle.load(open(sys.argv[1]))
for i in range(len(x)):
	print "[",i,"]"
	for j in range(len(x[i])):
		keys = x[i][j].keys()
		for k in range(len(keys)):
			print keys[k], x[i][j][keys[k]]
		print "\n"
	print "\n\n"