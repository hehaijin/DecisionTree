from sklearn import tree


trainset=DataSet()
testset=DataSet()

#Each row read from the csv file is returned as a list of strings.
with open('training.csv', newline='') as csvfile:
		trainreader = csv.reader(csvfile)
		for row in trainreader:
			p=Point(row[1],row[2])
			trainset.append(p)
			
clf = tree.DecisionTreeClassifier()
clf.fit()
			
			
			
			
