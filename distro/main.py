#!/usr/bin/python

import pickle
import two_level_classifier

print 'Performing classification of free apps...'
x = two_level_classifier.analyze_all_free()

print 'Performing classification of paid apps...'
y = two_level_classifier.analyze_all_paid()

pickle.dump(x, open('results/results_free.dat', 'w'))
pickle.dump(y, open('results/results_paid.dat', 'w'))