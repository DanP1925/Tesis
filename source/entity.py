import math
import heapq

class Entity:

	def __init__(self, name):
		self.name = name
		self.numberOfReviews = 0
		self.sentiments = []
		self.matrix = []
		
	def isInEntity(self, newSentiment):
		for sentiment in self.sentiments:
			if sentiment.isEqual(newSentiment):
				return True
		return False
		
	def addSentiment(self, newSentiment):
		if not self.isInEntity(newSentiment):
			self.sentiments.append(newSentiment)
			
	def minimumValue(self, targetList, k):
		auxSet = set(targetList)
		sortedSet = sorted(auxSet, reverse = True)
		if k<len(sortedSet):
			return sortedSet[k]
		else:
			return 0
			
	def generateGraph(self):
		for i in range(0,len(self.sentiments)):
			list = []
			for j in range(0,len(self.sentiments)):
				if i != j:
					list.append(self.sentiments[i].similarity(self.sentiments[j]))
				else:
					list.append(0)
			min = self.minimumValue(list, math.ceil(self.numberOfReviews/5))
			for element in list:
				if element < min:
					element = 0
			self.matrix.append(list)
			
	def initializeLeaders(self):
		h = 0
		heap = []
			
	def printMatrix(self):
		for i in range(0,len(self.sentiments)):
			for j in range(0, len(self.sentiments)):
				print(str(self.matrix[i][j]) + " ", end ='')
			print()
			
	def addReview(self):
		self.numberOfReviews += 1
	
	def debug(self):
		print('Entity')
		print(self.name)
		for sentiment in self.sentiments:
			sentiment.debug()