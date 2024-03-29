import nltk.collocations
import nltk.corpus
import collections

bgm    = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(
    nltk.corpus.movie_reviews.words())
scored = finder.score_ngrams( bgm.likelihood_ratio  )

# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])

print 'doctor', prefix_keys['doctor'][:5]
print 'baseball', prefix_keys['baseball'][:5]
print 'happy', prefix_keys['happy'][:5]