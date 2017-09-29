import csv
from classes import DataSet,Point,Node,Leaf
import sys


trainingfile=sys.argv[1]
testfile=sys.argv[2]
outputfile=sys.argv[3]
method=sys.argv[4]
chisquare=sys.argv[5]

print(trainingfile)
print(outputfile)

trainset=DataSet()
testset=DataSet()

#Each row read from the csv file is returned as a list of strings.
with open(trainingfile, newline='') as csvfile:
		trainreader = csv.reader(csvfile)
		for row in trainreader:
			p=Point(row[1],row[2])
			trainset.append(p)

#buiding the tree with different methods and different chisquare
#change parameters to use different methods and different chi square level.
treeroot=trainset.buildDecitionTree(method=method, chisquare=chisquare)


with open(testfile, newline='') as csvfile:
		testreader = csv.reader(csvfile)
		data=[]
		for row in testreader:
			p=Point(row[1])
			label=p.getLabel(treeroot)
			newrow=[]
			newrow.append(row[0])
			newrow.append(label)
			data.append(newrow)
			
with open(outputfile, "w") as csvfile:
		testwriter=csv.writer(csvfile)
		testwriter.writerow(["id","class"])
		for row in data:
			testwriter.writerow(row)	



	






