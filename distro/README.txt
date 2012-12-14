Dependencies
---------------------------------------------------------------------------
Python Packages
nltk
	- treebank corpus
	- movie_reviews corpus
numpy
scipy
matplotlib
scikit-learn

How to Run
---------------------------------------------------------------------------
Step 1: 
---------------------------------------------------------------------------
Run the following command which peforms the following:
	a) Reads in user revies from both free and paid applications
	b) Collects extracted phrases from reviews
	c) Performs Hierarchical classification on the reviews to predict ratings
	d) Performs a pickle.dump() of all results into 2 files.

Command:
--------
python main.py

Result:
--------
Two files containing all the information will be placed in the ./results folder.
	- results/
	- results/

---------------------------------------------------------------------------
Step 2:
---------------------------------------------------------------------------

Run the following command to view the results of all the steps performed in
Step 1. 

Command:
--------
python view.py

or 

python view.py > results.txt (to pipe the results into a file.)

---------------------------------------------------------------------------
Step 3:
---------------------------------------------------------------------------

Run the following command that performs an analysis of the results generated
from Step 1

Command:
--------
Free applications: 
python results_analyzer.py results/results_free.dat 

Paid applications:
python results_analyzer.py results/results_paid.dat




