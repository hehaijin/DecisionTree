import numpy as np
import math

valuedict={"A":0,"T":1,"G":2,"C":3,"N":0,"D":0, "R":0, "S":0}
labeldict={"EI":0,"IE":1,"N":2}



class Node:
	def __init__(self,value):
		self.value=value
		self.edges=[]

class Leaf(Node):
	def __init__(self, value):
		self.value=value

class Attribute():
	def _init_(self,name):
		self.name=name




class Point:
	def __init__(self,nucleotides,label="N"):
		self.label=label
		self.features={}
		for i in range(len(nucleotides)):
			self.features[i]=nucleotides[i]
	
	#def getLabel(self,TreeRoot):

	


class DataSet:
	def __init__(self):
		self.PointSet=[]
		self.labels=set()
		self.limit=0.1
		
		
	def append(self,point):
		self.PointSet.append(point)
		self.labels.add(point.label)
		
	
	def setLimit(self,limit):
		self.limit=limit
		
	def getFeatureNumber(self):
		if len(self.PointSet)==0:
			return 0
		else:
			return len(self.PointSet[0].features.keys())
	
	
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
					marginX[i]=marginX[i]+avc[i][j]
					#marginY[j]=marginY[j]+avc[i][j]	
			totalentropy=0
			for i in range(4):
				entropy=0
				for j in range(3):
					if avc[i][j]!=0:
						e=-1*avc[i][j]/marginX[i]* math.log2(avc[i][j]/marginX[i])
						entropy=entropy+e
				entropy=marginX[i]/total*entropy
				totalentropy=totalentropy+entropy
			entropies[attribute]=totalentropy
		
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
		
		result=0
		print(count)
		for i in range(3):
			if count[i]!=0:
				result=result-count[i]/total*math.log2(count[i]/total)
		return result
		
	
	def getAttributeGini(self):
		i=1
	
	def split(self,attribute):
		size=len(self.PointSet)
		data=[]
		for i in range(4):
			data[i]=DataSet()
		
		for i in range(size):
			self.PointSet[i].features.pop(attribute)
			label=self.PointSet[i].label
			data[labeldict[label]].add(self.PointSet[i])
			
		
	def buildDecitionTree(self):
		attri, entro=self.getAttributeInfoGain()
		c=self.getEntropy()
		mlabel=self.getMajorityLabel()
		if c-entro >= self.limit:
			root=Node(attri)
			print("adding root "+str(attri))
			size=len(self.PointSet)
			data=[]
			for i in range(4):
				data.append(DataSet())
			for i in range(size):
				
				v=self.PointSet[i].features[attri]
				self.PointSet[i].features.pop(attri)
				data[valuedict[v]].append(self.PointSet[i])
			for i in range(4):
				print(len(data[i].PointSet))
				data[i].buildDecisionTreefrom(root,mlabel)
		
		
		
		
		
		return root
			
	def getMajorityLabel(self):
		labelcount={}
		count=np.zeros(3)
		for i in range(len(self.PointSet)):
			label=self.PointSet[i].label
			count[labeldict[label]]=count[labeldict[label]]+1
		
		m=max(count)
		for i in range(3):
			if count[i]==m:
				t=i
		for k in labeldict.keys():
			if labeldict[k]==t:
				return k
		
		
		
		
	
	def buildDecisionTreefrom(self,upperNode,majoritylabel):
		
		if len(self.PointSet)==0:
			lf=Leaf(majoritylabel)
			upperNode.edges.append(lf)
			return
		if len(self.PointSet) <10:
			lf=Leaf(self.getMajorityLabel())
			upperNode.edges.append(lf)
			return
		if self.getFeatureNumber() !=0:
			attri, entro=self.getAttributeInfoGain()
			c=self.getEntropy()
			print("entropy gain")
			print(c)
			print(entro)
			print(c-entro)
			if c-entro >= self.limit:
				#adding subnode
				n=Node(attri)
				upperNode.edges.append(n)
				
				#splitting
				size=len(self.PointSet)
				data=[]
				for i in range(4):
					data.append(DataSet())
			
				for i in range(size):
					v=self.PointSet[i].features[attri]
					self.PointSet[i].features.pop(attri)
					data[valuedict[v]].append(self.PointSet[i])
				for i in range(4):
					data[i].buildDecisionTreefrom(n,majoritylabel)
		else:
			lf=Leaf(self.getMajorityLabel())
			upperNode.edges.add(lf)
			
		


	def shouldStop(self):
		entropy=self.getEntropy()
		k,m=self.getAttributeInfoGain()
		if  entropy-m < limit:
			return False
		else:
			 return True














