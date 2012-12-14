#!/usr/bin/python

import string

PUNCTUATION = ['.', '?', '!', ',']

def clean_sentence(s):
	if s[-1] in PUNCTUATION and s[-2] not in PUNCTUATION:
		s = s[:-1] + ' ' + s[-1]
	
	comma_index_list = []
	for i in range(len(s)):
		if s[i] == ',':
			comma_index_list.append(i)
	temp = ""
	last_index = 0
	for i in range(len(comma_index_list)):
		cur_index = comma_index_list[i]
		temp = temp + s[last_index:cur_index] + ' , '
		last_index = cur_index + 1
	temp = temp + s[last_index:]
	s = temp
	
	return s

if __name__ == '__main__':
	s = raw_input('Type a sentence: ')
	print clean_sentence(s)