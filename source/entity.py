import math
import heapq

class Entity:

	def __init__(self, name):
		self.name = name
		self.numberOfReviews = 0
		self.sentiments = []
		self.matrix = []
		self.leaders = []
		
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
			self.sentiments[i].calculateDegree(list)
			self.matrix.append(list)
	
	def obtainHNodes(self):
		h = 0
		i=0
		heap = []
		for sentiment in self.sentiments:
			if (h==0 and sentiment.degree!=0):
				heapq.heappush(heap,(sentiment.degree,i))
				h += 1
			else:
				if (sentiment.degree>h and heap[0][0] > h):
					heapq.heappush(heap,(sentiment.degree,i))
					h += 1
				elif (sentiment.degree>h and heap[0][0] == h):
					heapq.heappop(heap)
					heapq.heappush(heap,(sentiment.degree,i))
			i+=1
		return heap
	
	def hasLeaderNeighbors(self, hnode):
		for index in self.leaders:
			if self.matrix[hnode[1]][index] >0:
				return True
		return False
	
	def initializeLeaders(self):
		hnodes = self.obtainHNodes()
		hnodes.sort(reverse=True)
		print(hnodes)
		while len(hnodes) != 0:
			hnode = hnodes.pop(0)
			if not self.hasLeaderNeighbors(hnode):
				self.leaders.append(hnode[1])
		print(self.leaders)
			
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