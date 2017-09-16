import csv
from classes import DataSet,Point


dataset=DataSet()

with open('training.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			p=Point(row[1],row[2])
			dataset.append(p)








a,b=dataset.getAttributeInfoGain()
print(a)

b=dataset.getEntropy()
print(b)
