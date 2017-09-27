import csv
from classes import DataSet,Point,Node,Leaf



trainset=DataSet()
testset=DataSet()

#Each row read from the csv file is returned as a list of strings.
with open('training.csv', newline='') as csvfile:
		trainreader = csv.reader(csvfile)
		for row in trainreader:
			p=Point(row[1],row[2])
			trainset.append(p)

#buiding the tree with different methods and different chisquare
treeroot=trainset.buildDecitionTree(method="gini",chisquare="99")


with open('testing.csv', newline='') as csvfile:
		testreader = csv.reader(csvfile)
		data=[]
		for row in testreader:
			p=Point(row[1])
			label=p.getLabel(treeroot)
			newrow=[]
			newrow.append(row[0])
			newrow.append(label)
			data.append(newrow)
			
with open('result.csv', "w") as csvfile:
		testwriter=csv.writer(csvfile)
		testwriter.writerow(["id","class"])
		for row in data:
			testwriter.writerow(row)	



	






