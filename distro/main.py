#!/usr/bin/python

import pickle
import two_level_classifier

x = two_level_classifier.analyze_all_free()
y = two_level_classifier.analyze_all_paid()

pickle.dump(x, open('results/results_free.dat', 'w'))
pickle.dump(y, open('results/results_paid.dat', 'w'))