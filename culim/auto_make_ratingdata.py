#!/usr/bin/python

import pickle
import two_level_classifier

x = two_level_classifier.analyze_all_free()
y = two_level_classifier.analyze_all_paid()

pickle.dump(x, open('test_freerat.dat', 'w'))
pickle.dump(y, open('test_paidrat.dat', 'w'))