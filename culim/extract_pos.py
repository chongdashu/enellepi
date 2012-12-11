from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize, WhitespaceTokenizer

import enellepi
import pickle
import pprint

'''
Tag patterns for extracting two-word phrases from reviews.
@see Turney paper
'''
TAG_PATTERNS_2WORD = [
	['JJ|JJS|JJR',				'NN|NNS', 			''],
	['RB|RBR|RBS', 				'JJ|JJS|JJR', 		'not-NN^not-NNS'],
	['JJ|JJS|JJR',				'JJ|JJS|JJR',		'not-NN^not-NNS'],
	['NN|NNS',					'JJ|JJS|JJR',		'not-NN^not-NNS'],
	['RB|RBR|RBS',				'VB|VBD|VBN|VBG',	''],
	['DT',						'JJ|JJS|JJR', 		''],
	['VBZ',						'JJ|JJS|JJR', 		'']
]

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def match(tag, pos_tag):
	if (tag == ''):
		return True
	if (len(tag.split('-')) > 1):
		return pos_tag[1] != tag.split('-')[1]
	return pos_tag[1] == tag

def do_pos_tags_match_pattern(pos_tags, pattern):

	first_tags = pattern[0].split('|')
	second_tags = pattern[1].split('|')
	third_tags = pattern[2].split('^')

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

	matched_third = True;
	for tag in third_tags:
		if match(tag, pos_tags[2]):
			matched_third = matched_third and match(tag, pos_tags[2])
	if matched_third:
		print 'matched third word for tags:' + str(third_tags) + ', pos_tag:' + str(pos_tags[2])

	return matched_first and matched_second and matched_third

def get_phrases_from_text(text):
	phrases = []

	# First, we split the reviews into sentences/
	sentences = sent_tokenize(text)

	for sentence in sentences:
		'''
		For each sentence, we tokenize the text into word tokens.
		Next, we run the POS tagging on the tokens.
		'''
		text_tokenized = word_tokenize(sentence)
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

def extract_all():
	'''
	'phrases_free' is a dictionary.
	It is indexed by the the review-index.
	'''
	phrases_free = {}
	for i in range(len(free_reviews)):
		phrases = get_phrases_from_text(free_reviews[i]['text'])
		phrases_free[i] = phrases


	'''
	'phrases_paid' is a dictionary.
	It is indexed by the the review-index.
	'''
	phrases_paid = {}
	for i in range(len(paid_reviews)):
		phrases = get_phrases_from_text(paid_reviews[i]['text'])
		phrases_paid[i] = phrases


	'''
	Uncomment when wish to write to file.
	'''
	f = open('data/phrases_2word_free.dat', 'w')
	pickle.dump(phrases_free, f)
	f.close()

	'''
	Uncomment when wish to write to file.
	'''
	f = open('data/phrases_2word_paid.dat', 'w')
	pickle.dump(phrases_paid, f)
	f.close()

file = open("data/topfree.dat", 'r')
free_reviews = pickle.load(file)
file.close()

file = open("data/toppaid.dat", 'r')
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








