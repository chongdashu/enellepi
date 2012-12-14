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
	- results/results_free.dat
	- results/results_paid.dat

Note:
--------
Because the classifier in this case uses SVMs from the scikit-learn package, 
in the event trouble is encountered with producing the resulting .dat files, 
we have provided the .dat files in the folder /backup_results/

---------------------------------------------------------------------------
Step 2:
---------------------------------------------------------------------------

Run the following command to view the results of all the steps performed in
Step 1. 

Command:
--------
Free applications:
python view.py results/results_free.dat 
python view.py results/results_free.dat > results_free.txt 

Paid applications:
python view.py results/results_paid.dat 
python view.py results/results_paid.dat > results_paid.txt

Result:
--------
Shows every example in the dataset, each entry containing the following fields:
 - rating-user: the original rating given by the user
 - title-cls: polarity classification of the title
 - title: the title of the review
 - text: the text of the review
 - text-cls: polarity classification of the text
 - original_index: the index of the review before the shuffling was performed
 - rating calculated: predicted star-rating of the review. 

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

Result:
--------
Shows every example in the dataset, the original user rating and our predicted rating.
At the end, a summary on data including the accuracy and performance is printed.




