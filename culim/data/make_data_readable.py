#!/usr/bin/python

import pickle
import sys

x = pickle.load(open(sys.argv[1]))
for i in range(len(x)):
	print "[",i,"]"
	keys = x[i].keys()
	for j in range(len(keys)):
		print "-",keys[j],"-"
		if keys[j] == "info":
			keys_keys = x[i][keys[j]].keys()
			for k in range(len(keys_keys)):
				print keys_keys[k],":",x[i][keys[j]][keys_keys[k]]
		if keys[j] == "phrases":
			p_list = x[i][keys[j]]
			for k in range(len(p_list)):
				print x[i][keys[j]][k]
		print "\n"
	print "\n\n"
