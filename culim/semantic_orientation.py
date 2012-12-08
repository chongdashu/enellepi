import google_query
import pickle
import time
import pprint

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
	"Bad",
	"Okay",
	"Good",
	"Excellent"
]

pp = pprint.PrettyPrinter()
pp = pp.pprint

'''
Get all the reviews for the top free apps.
'reviews' is a dictionary, where:
	key: review-index
	value: array of phrases extracted from that review.
'''
data = pickle.load(open('topfree.dat'))
reviews = pickle.load(open('phrases_2word_free.dat'));

dict = {}
# Get a five-star review
review_five_star = data[2]
review_five_star_phrases = reviews[2]
for phrase in review_five_star_phrases:
	(word1, tag1) = phrase[0]
	(word2, tag2) = phrase[1]
	for keyword in KEYWORDS:
		query = '"' + word1 + '"' + '+' + word2 + '"' + ' AROUND(10) ' + keyword
		print 'query:' + query
		time.sleep(1.0)
		hits = google_query.get_hit_count(query)
		dict[(word1 + '+' + word2, keyword)] = hits
