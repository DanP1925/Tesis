import opinionNode as NOD
import math
import heapq

class opinionGraph:
		
	def __init__(self):
		self.nodes = []
		self.k = 0
		
	def setNeighborNumber(self,reviews):
		numOfSentiments = 0
		for review in reviews:
			for sentiment in review.sentiments:
				numOfSentiments += 1
		self.k = math.ceil(numOfSentiments/5)
			
	def setNodes(self, reviews):
		for review in reviews:
			for sentiment in review.sentiments:
				if not self.hasNode(sentiment):
					newNode = NOD.opinionNode(sentiment)
					self.nodes.append(newNode)
		
	def setEdges(self):
		for node in self.nodes:
			node.setEdges(self.nodes, self.k)
	
	def hasNode(self, sentiment):
		for node in self.nodes:
			if node.sentiment.text == sentiment.text:
				return True
		return False
	
	def obtainHNodes(self):
		h = 0
		i = 0
		heap = []
		for node in self.nodes:
			if (h==0 and node.degree!=0):
				heapq.heappush(heap,(node.degree,i))
				h += 1
			else:
				if (node.degree>h and heap[0][0] > h):
					heapq.heappush(heap,(node.degree,i))
					h += 1
				elif (node.degree>h and heap[0][0] == h):
					heapq.heappop(heap)
					heapq.heappush(heap,(node.degree,i))
			i+=1
		return heap
		
	def hasLeaderNeighbors(self, index, leaders):
		for leader in leaders:
			if self.nodes[index].edges[leader] >0:
				return True
		return False
	
	def setDistances(self, leaders):
		selfIndex = 0
		for node in self.nodes:
			node.setDistances(leaders, selfIndex)
			selfIndex += 1
	
	def getDistances(self):
		distances = []
		for index in range(0,len(self.nodes)):
			distances.append([index,self.nodes[index].distances])
		return distances
			
	def edgesWithCommunity(self, index,community):
		num = 0
		edges = self.nodes[index].edges
		for i in range(0,len(edges)):
			if edges[i] > 0:
				if i in community.elements:
					num += edges[i]
		return num
	
	def printMatrix(self):
		for node in self.nodes:
			print(node.sentiment.text)
			print(node.edges)