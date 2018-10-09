# DecisionTree
Decision Tree practical including post pruning

The driver.py file contains an absolute path which needs to be changed before implementing.

combined.py file contains the full code combining driver.py and DecisionTree.py, so it is easy to run just the one file containing all the code. You don't have to worry about any absolute path in this file.

The haberman's survival dataset is used to test the model.

Some part of data is kept for validation purposes.

The Haberman's survival dataset cantains 305 rows and 4 attributes which can be used to split upon.

There are 4 features including class label.

1. age of the patient
2. the operation year
3. number of positive auxillary nodes detected
4. the survival status- 1 = patient survived atleast 5 years, and 2 = patient died within 5 years.

Various nodes can be pruned in order to obtain more test and training accuracy.

The size of validation dataset can also be changed to check for overfitting prior to executing it on the test data. 
