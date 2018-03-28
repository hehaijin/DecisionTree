import numpy as np
import math

valuedict={"A":0,"T":1,"G":2,"C":3,"N":0,"D":0, "R":3, "S":3}
labeldict={"EI":0,"IE":1,"N":2}
chisquaretable={"99":14.7,"95":12.592,"0":0 }                #chi-square table for freedom 6


#for decision tree node except leaf
class Node:
	def __init__(self,value):
		self.value=value
		self.edges=[]

#decision tree leaf node
class Leaf(Node):
	def __init__(self, value):
		self.value=value


#attribute 
class Attribute():
	def _init_(self,name):
		self.name=name



#one data entry line
class Point:
	def __init__(self,nucleotides,label="N"):
		self.label=label
		self.features={}
		for i in range(len(nucleotides)):
			self.features[i]=nucleotides[i]
	
	def getLabel(self,TreeRoot):
		if isinstance(TreeRoot,Leaf):
			return TreeRoot.value
		else:
			v=TreeRoot.value
			index=valuedict[self.features[v]]
			node=TreeRoot.edges[index]
			return self.getLabel(node)

	

# a collections of data points
#includes methods that calculate entropy, gini index, build decision tree.
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
	
	#get the attribute to split the data set based on info gain method
	#return the attribute and the entropy after split
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
			
		
		
		
		
		
		
	#cauculate entropy for the dataset.	
	
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
		#print(count)
		for i in range(3):
			if count[i]!=0:
				result=result-count[i]/total*math.log2(count[i]/total)
		return result
		
	#get the attribute to split the data set based on gini index method
	#return the attribute and the gini index after split
	def getAttributeGini(self):
		total=len(self.PointSet)
		ginis={}
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
					marginY[j]=marginY[j]+avc[i][j]
			
				
			totalgini=0;
			for i in range(4):
				c=1
				for j in range(3):
					if marginX[i]==0:
						c=c
					else:
						c=c-avc[i][j]*avc[i][j]/marginX[i]/marginX[i];
				totalgini=totalgini+c
			ginis[attribute]=totalgini
		#print(ginis)
		m=min(ginis.values())  #this could be nan
		for k,v in ginis.items():
			if v==m:
				return (k,m)	
		
		
			
	#build decision tree using current data set as root node of the tree
	def buildDecitionTree(self,method="infogain",chisquare="99"):
		if method=="infogain":
			attri, entro=self.getAttributeInfoGain()
		else:
			attri,entro=self.getAttributeGini()
		print("method is"+method)
		c=self.getEntropy()
		mlabel=self.getMajorityLabel()
		#if c-entro >= self.limit:
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
			print("the size of the splitted tree is "+str(len(data[i].PointSet)))
			data[i].buildDecisionTreefrom(root,mlabel,method,chisquare)
	
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
		
		
		
		
	#building decision tree but the current node is not root node.
	#for recurrsion call
	def buildDecisionTreefrom(self,upperNode,majoritylabel,method, chisquare):
		
		if len(self.PointSet)==0:
			lf=Leaf(majoritylabel)
			upperNode.edges.append(lf)
			return
		if len(self.PointSet) <2:
			lf=Leaf(self.getMajorityLabel())
			upperNode.edges.append(lf)
			return
		if self.getFeatureNumber() !=0:
			cslimit= chisquaretable[chisquare]
			
			if method=="infogain":
				attri, entro=self.getAttributeInfoGain()
			else:
				attri, entro=self.getAttributeGini()
			c=self.getEntropy()
			cs=self.chisquare(attri)
			#the stopping criteria 
			if cs >= cslimit or cslimit==0 :
			#if c-entro>0.1:
				#adding subnode
				n=Node(attri)
				#print("splitting at attr "+ str(attri))
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
					data[i].buildDecisionTreefrom(n,majoritylabel,method,chisquare)
			else:
				lf=Leaf(self.getMajorityLabel())
				upperNode.edges.append(lf)
		else:
			lf=Leaf(self.getMajorityLabel())
			upperNode.edges.append(lf)
			
		



			 
			 
	#calculating chi square for an atribute for the dataset		 
	def chisquare(self, attr):
		total=len(self.PointSet)
		count=np.zeros(3)
		for i in range(len(self.PointSet)):
			label=self.PointSet[i].label
			count[labeldict[label]]=count[labeldict[label]]+1
		avc=np.zeros((4,3)) #avc table
		marginX=np.zeros(4)
		print(count)
		for i in range(len(self.PointSet)):
			v=self.PointSet[i].features[attr]
			l=self.PointSet[i].label
			avc[valuedict[v],labeldict[l]]=avc[valuedict[v],labeldict[l]]+1
		for i in range(4):
			for j in range(3):
				marginX[i]=marginX[i]+avc[i][j]
		chisquare=0
		for i in range(4):
			for j in range(3):
				expect=count[j]/total*marginX[i]
				if expect==0:
					chisqure=chisquare
				else:
					chisquare=chisquare+ (avc[i][j]-expect)*(avc[i][j]-expect)/expect
		print("chi square for attribute "+ str(attr)+" is "+ str(chisquare))
		return chisquare












