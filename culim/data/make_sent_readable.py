#!/usr/bin/python

import pickle
import sys

x = pickle.load(open(sys.argv[1]))
for i in range(len(x)):
	print "[",i,"]"
	keys = x[i].keys()
	for j in range(len(keys)):
		print keys[j],":", x[i][keys[j]]
	print "\n\n"
