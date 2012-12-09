import google_query
import pickle
import time
import pprint
import random
import math

import concordance

'''
Keywords used as a measure against each review's star-rating. 
Quite obviously which values map to which, but for clarity:
	1-Star: 	Poor
	2-Stars:	Bad
	3-Stars:	Okay
	4-Stars:	Good
	5-Stars:	Excellent
'''
KEYWORDS = [
	"Poor",
	"Excellent"
]

HITS_POOR = 70400000.0
HITS_EXCELLENT = 112000000.0

so_dict_free = {}
so_dict_paid = {}

def replace_contractions(word):
	'''
	Replaces tokenized words like ('t) into (not).
	'''
	if word == "n't":
		return "not"
	return word

'''
Some useful printing methods.
Do 'pprint' to pretty print things.
'''
pp = pprint.PrettyPrinter()
pprint = pp.pprint

'''
Seed the randomizer.
'''
random.seed(time.clock())

'''
Get all the reviews for the top free apps.
'reviews' is a dictionary, where:
	key: review-index
	value: array of phrases extracted from that review.
'''
data = pickle.load(open('topfree.dat'))
reviews = pickle.load(open('phrases_2word_free.dat'));

data2 = pickle.load(open('toppaid.dat'))
reviews2 = pickle.load(open('phrases_2word_paid.dat'));

def get_near_query(phrase, keyword):
	'''
	Creates a query for a phrase around a keyword.
	@phrase: 	A 2-element list. Each element is a (word, tag) pair.
	@keyword:	String of the keyword to be near to.
	'''
	(word1, tag1) = phrase[0]
	(word2, tag2) = phrase[1]

	word1 = replace_contractions(word1)
	word2 = replace_contractions(word2)

	query = '"' + word1 + '+' + word2 + '"' + ' AROUND(10) ' + '"' + keyword + '"'

	return query

def calculate_semantic_orientation(phrase):
	'''
	Calculates the semantic orientation of a given phrase
	@phrase A 2-element list. Each element is a (word, tag) pair.
	'''
	query_near_excellent = get_near_query(phrase, 'excellent')
	query_near_poor = get_near_query(phrase, 'poor')

	time.sleep(5.0 + 5*random.random())
	hits_near_excellent = float(google_query.get_hit_count(query_near_excellent))
	time.sleep(5.0 + 5*random.random())
	hits_near_poor = float(google_query.get_hit_count(query_near_poor))

	ratio = (hits_near_excellent * HITS_POOR + 1E-9) /  (hits_near_poor * HITS_EXCELLENT + 1E-9)
	log_ratio = math.log(ratio)

	data = { 	'phrase' : phrase,
				'query_near_excellent' : query_near_excellent,
				'query_near_poor' : query_near_poor,
				'hits_near_excellent' : hits_near_excellent,
				'hits_near_poor' : hits_near_poor,
				'ratio' : ratio,
				'log_ratio' : log_ratio
	}

	return data

def calculate_semantic_orientation_dist(phrase):
	(word1, tag1) = phrase[0]
	(word2, tag2) = phrase[1]

	word1 = replace_contractions(word1)
	word2 = replace_contractions(word2)
	word1 = word1.encode('ascii', 'ignore');
	word2 = word2.encode('ascii', 'ignore');
	
	posd = concordance.OrientationDist(word1, word2, True);
	negd = concordance.OrientationDist(word1, word2, False);

	ratio = negd/posd;
	log_ratio = math.log(ratio);

	data = { 	'phrase' : phrase,
				'query_near_excellent' : "",
				'query_near_poor' : "",
				'hits_near_excellent' : posd,
				'hits_near_poor' : negd,
				'ratio' : ratio,
				'log_ratio' : log_ratio
	}
	return data;

def calculate_all_free(n=50, start_offset=0):
	print '***WARNING***\nThis is going to take a long time!\nIt also will make thousands of queries to Google, which might get your IP blocked!\nAre you sure you wish to continue?\n'
	
	so_dict = {}

	confirmation = raw_input('Type "yes" to begin: ')
	if confirmation == 'yes':
		print 'Here goes!'

		for i in range(start_offset, start_offset + n):
			print i
			phrases = reviews[i]
			so_dict[i] = []
			for phrase in phrases:
				so = calculate_semantic_orientation(phrase)
				so_dict[i].append(so)
	else:
		print 'Wise choice...'

	so_dict_free = so_dict
	return so_dict

def calculate_all_paid(n=50, start_offset=0):
	print '***WARNING***\nThis is going to take a long time!\nIt also will make thousands of queries to Google, which might get your IP blocked!\nAre you sure you wish to continue?\n'
	
	so_dict = {}

	confirmation = raw_input('Type "yes" to begin: ')
	if confirmation == 'yes':
		print 'Here goes!'

		for i in range(start_offset, start_offset + n):
			print i
			phrases = reviews2[i]
			so_dict[i] = []
			for phrase in phrases:
				so = calculate_semantic_orientation(phrase)
				so_dict[i].append(so)
	else:
		print 'Wise choice...'

	so_dict_paid = so_dict
	return so_dict

def example1():
	'''
	This example gets a review from a user from one of the top free apps.
	It takes a phrase from the review, and then calculates the semantic orientation of it.
	This uses the hit-distance ratio obtained by querying Google.
	'''
	review = reviews[0]		# Get the review for the first app.
	phrase = review[1]		# Get the second phrase extracted from the review.
	so = calculate_semantic_orientation(phrase)	# calculate semantic orientation of the phrase.
	pprint(so)				# Pretty print the results.



def example2():
	'''
	This example gets a review from a user from one of the top free apps.
	It takes a phrase from the review, and then calculates the semantic orientation of it.
	This uses a distance metric.
	'''
	review = reviews[0]		# Get the review for the first app.
	phrase = review[1]		# Get the second phrase extracted from the review.
	so = calculate_semantic_orientation_dist(phrase)	# calculate semantic orientation of the phrase.
	pprint(so)	

