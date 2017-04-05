import review as REV
import heapq
import opinionGraph as GRAPH

class Entity:

	def __init__(self, name):
		self.name = name
		self.reviews = []
		self.graph = GRAPH.opinionGraph()
		self.matrix = []
		self.leaders = []

	def addReview(self,tweet):
		newReview = REV.review(tweet)
		self.reviews.append(newReview)
		
	def minimumValue(self, targetList, k):
		auxSet = set(targetList)
		sortedSet = sorted(auxSet, reverse = True)
		if k<len(sortedSet):
			return sortedSet[k]
		else:
			return 0
			
	def obtainLeaders(self):
		self.graph.setNodes(self.sentiments)
		self.graph.setEdges(self.sentiments)
		return 0
	
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
		while len(hnodes) != 0:
			hnode = hnodes.pop(0)
			if not self.hasLeaderNeighbors(hnode):
				self.leaders.append(hnode[1])
			
	def minDist(self, unvisited):
		min = float("inf")
		index = -1
		for i in range(0,len(unvisited)):
			if unvisited[i][1] < min:
				min = unvisited[i][1]
				index = i
		return index

	def isInUnvisited(self, index, unvisited):
		for element in unvisited:
			if element[0] == index:
				return True
		return False
		
	def getNeighbors(self, index, unvisited):
		neighbors = []
		for i in range(0,len(self.matrix[index])) :
			if self.matrix[index][i] > 0 and self.isInUnvisited(index,unvisited):
				neighbors.append(i)
		return neighbors
		
	def getDistanceOfUnvisited(self, unvisited, neighbor):
		for element in unvisited:
			if element[0] == neighbor:
				return element[1]
				
	def setDistanceOfUnvisited(self, alt, unvisited, neighbor):
		for element in unvisited:
			if element[0] == neighbor:
				element[1] = alt
				break
		
	def dijkstra(self, target, leader):
		unvisited = []
		
		for u in range(0,len(self.matrix)):
			dist = float("inf")
			node = [u,dist]
			unvisited.append(node)
			
		unvisited[leader][1] = 0
		
		while len(unvisited) > 0:
			index = self.minDist(unvisited)
			v = unvisited[index]
			neighbors = self.getNeighbors(v[0], unvisited)
			for neighbor in neighbors:
				if neighbor == target:
					return self.getDistanceOfUnvisited(unvisited,neighbor)
				alt = v[1] + 1
				if alt < self.getDistanceOfUnvisited(unvisited,neighbor):
					self.setDistanceOfUnvisited(alt, unvisited,neighbor)
			unvisited.pop(index)
		return float("inf")
			
	def getDistances(self):
		distances = []
		for i in range(0,len(self.matrix)):
			distance = []
			for leader in self.leaders:
				distance.append(1)
				distance.append(self.dijkstra(i,leader))
			distances.append((distance,i))
		return distances
			
	def printMatrix(self):
		for i in range(0,len(self.sentiments)):
			for j in range(0, len(self.sentiments)):
				print(str(self.matrix[i][j]) + " ", end ='')
			print()
	
	def debug(self):
		print('Entity')
		print(self.name)
		for sentiment in self.sentiments:
			sentiment.debug()