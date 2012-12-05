from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

import enellepi
import pickle

'''
Tag patterns for extracting two-word phrases from reviews.
@see Turney paper
'''
TAG_PATTERNS_2WORD = [
	['JJ', 			'NN|NNS', 	''],
	['RB|RBR|RBS', 	'JJ', 		'not-NN)|not-NNS)'],
	['JJ',			'JJ',		'not-NN)|not-NNS)'],
	['NN|NNS',		'JJ',		'not-NN)|not-NNS)'],
	['RB|RBR|RBS',	'VB|VBD|VBN|VBG',	'']
]

def match(tag, pos_tag):
	if (tag == ''):
		return True
	if (len(tag.split('-')) > 1):
		return pos_tag[1] != tag.split('-')[1]
	return pos_tag[1] == tag

def do_pos_tags_match_pattern(pos_tags, pattern):

	first_tags = pattern[0].split('|')
	second_tags = pattern[1].split('|')
	third_tags = pattern[2].split('|')

	print '----------------------------------------------------'
	print 'pattern: ' + str(pattern)
	print 'pos_tags:' + str(pos_tags)

	matched_first = False;
	for tag in first_tags:
		if match(tag, pos_tags[0]):
			print 'matched first word for tag:' + tag + ', pos_tag:' + str(pos_tags[0])
			matched_first = True
			break

	matched_second = False;
	for tag in second_tags:
		if match(tag, pos_tags[1]):
			print 'matched second word for tag:' + tag + ', pos_tag:' + str(pos_tags[1])
			matched_second = True
			break

	matched_third = False;
	for tag in third_tags:
		if match(tag, pos_tags[2]):
			print 'matched third word for tag:' + tag + ', pos_tag:' + str(pos_tags[2])
			matched_third = True
			break

	return matched_first and matched_second and matched_third

def get_phrases_from_text(text):
	phrases = []

	text_tokenized = word_tokenize(text)
	text_pos_tags = pos_tag(text_tokenized)

	for i in range(len(text_pos_tags)):
		if i+2 >= len(text_pos_tags):
			break
		for pattern in TAG_PATTERNS_2WORD:
			pos_tags = [text_pos_tags[i], text_pos_tags[i+1], text_pos_tags[i+2]]
			# print 'matching pos_tags:' + str(pos_tags) + ' with pattern:' + str(pattern)
			if do_pos_tags_match_pattern(pos_tags, pattern):
				print 'found pattern match, adding: ' + str(pos_tags[:2])
				phrases.append(pos_tags[:2])
				continue

	return phrases

file = open("topfree.dat", 'r')
free_reviews = pickle.load(file)
file.close()

file = open("toppaid.dat", 'r')
paid_reviews = pickle.load(file)
file.close()

'''
	Test sentence.
'''
'''
sentence = 'The fat man was hungry today.'
sentence_token = word_tokenize(sentence)
sentence_pos = pos_tag(sentence_token)
phrase = get_phrases_from_text(sentence)
'''

all_phrases = []
for i in range(100):
	phrases = get_phrases_from_text(free_reviews[i]['text'])
	all_phrases = all_phrases + phrases


