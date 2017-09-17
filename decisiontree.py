import csv
from classes import DataSet,Point


trainset=DataSet()
testset=DataSet()

with open('training.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			p=Point(row[1],row[2])
			trainset.append(p)

with open('testing.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			p=Point(row[1])
			testset.append(p)




