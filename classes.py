import numpy as np
import math

valuedict={"A":0,"T":1,"G":2,"C":3,"N":0,"D":0, "R":0, "S":0}
labeldict={"EI":0,"IE":1,"N":2}




class Attribute():
	def _init_(name):
		self.name=name




class Point:
	def __init__(self,nucleotides,label):
		self.label=label
		self.features={}
		for i in range(len(nucleotides)):
			self.features[i]=nucleotides[i]
		

	

	


class DataSet:
	
	
	def __init__(self):
		self.PointSet=[]
		self.labels=set()
		
		
	def append(self,point):
		self.PointSet.append(point)
		self.labels.add(point.label)
	
	
	
	def getAttributeInfoGain(self):
		entropies={}
		total=len(self.PointSet)
		for attribute in self.PointSet[0].features.keys():
			avc=np.zeros((4,3))
			marginX=np.zeros(4)
			marginY=np.zeros(3)
			for i in range(len(self.PointSet)):
				v=self.PointSet[i].features[attribute]
				l=self.PointSet[i].label
				
				avc[valuedict[v],labeldict[l]]=avc[valuedict[v],labeldict[l]]+1
			
			for i in range(4):
				for j in range(3):
					if avc[i][j]==0:
						avc[i][j]=1
					marginX[i]=marginX[i]+avc[i][j]
					marginY[j]=marginY[j]+avc[i][j]	
			totalentropy=0
			for i in range(4):
				entropy=0
				for j in range(3):
					e=-1*avc[i][j]/marginY[j]* math.log2(avc[i][j]/marginY[j])
					entropy=entropy+e
				entropy=marginX[i]/total*entropy
				totalentropy=totalentropy+entropy
			entropies[attribute]=totalentropy
		#print(entropies)
		m=min(entropies.values())	
		for k,v in entropies.items():
			if v==m:
				return (k,m)
			
		
		
		
		
		
		
		
	def getEntropy(self):
		total=len(self.PointSet)
		count=np.zeros(3)
		for i in range(total):
			if self.PointSet[i].label=="EI":
				count[0]=count[0]+1
			if self.PointSet[i].label=="IE":
				count[1]=count[1]+1
			if self.PointSet[i].label=="N":
				count[2]=count[2]+1
		#print(count)
		result=0
		for i in range(3):
			result=result-count[i]/total*math.log2(count[i]/total)
		return result
	
	def getAttributeGini(self):
		i=1
	
	def split():
		i=1


	def shouldStop():
		i=1














