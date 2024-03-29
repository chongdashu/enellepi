#!/usr/bin/python
import simplejson as json
import urllib
import pickle
import types

def google_search(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

def get_hit_count(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  
  #if the search result is null, return 0 for the number of hits for that phrase
  if isinstance(data, types.NoneType):
    return 0

  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

  if ('estimatedResultCount' in data['cursor']):
    return data['cursor']['estimatedResultCount']
  else:
    return 0

'''
  Load all the 2-word phrases which were extracted.
'''
# phrases = pickle.load(open('data/phrases_2word_free.dat'));

'''
  Sample execution of a Google query for a given phrase.
'''
'''
review = phrases[0]
test_phrase = review[1]
query = "{0} {1}".format(test_phrase[0][0], test_phrase[1][0])
print 'query:' + query
hits = get_hit_count(query)
'''