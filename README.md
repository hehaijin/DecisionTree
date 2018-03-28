# DecisionTree
Implementation of decision tree algorithm(ID3) for Machine Learning(cs529) class
coded in Python 3.6


executeable file: decisiontree.py

execute format:

python decisiontree.py trainingfile testfile outputfile method chisquare

for example

python decisiontree.py training.csv testing.csv result.csv infogain 99

python decisiontree.py training.csv testing.csv result.csv infogain 0

python decisiontree.py training.csv testing.csv result.csv gini 95

related classes are put in classes.py
the DataSet class 's buildDecitionTree() method is the method for building decision tree on that data set.
to use different methods:

other annoation can be found along side the code. 








