class opinionNode:

		def __init__(self, sentiment):
			self.sentiment = sentiment
			self.degree = 0
			self.score = 0
			self.distances = []
			self.edges = []
			
		def setEdges(self, nodes, k):
			edges = []
			for node in nodes:
				if self.sentiment.text == node.sentiment.text:
					edges.append(0)
				else:
					edges.append(self.sentiment.similarity(node.sentiment))
			
			min = self.minimumValue(edges, k)
			index = 0
			for index in range(0,len(edges)):
				if edges[index] < min:
					edges[index] = 0
				index += 1
			self.calculateDegree(edges)
			self.edges = edges
			
		def minimumValue(self, targetList, k):
			auxSet = set(targetList)
			sortedSet = sorted(auxSet, reverse = True)
			if k<len(sortedSet):
				return sortedSet[k-1]
			else:
				return 0
			
		def calculateDegree(self, list):
			degree = 0
			for element in list:
				if element > 0:
					degree +=1
			self.degree = degree
			
		def setDistances(self, leaders, selfIndex):
			for leader in leaders:
				self.distances.append(self.dijkstra(leader, selfIndex))
				
		def dijkstra(self, target, selfIndex):
			unvisited = []
			
			for index in range(0,len(self.edges)):
				dist = float("inf")
				node = [index,dist]
				unvisited.append(node)
				
			self.setDistanceOfUnvisited(unvisited, selfIndex, 0)

			while len(unvisited) != 0:
				minIndex = self.getMinFromUnvisited(unvisited)
				node = unvisited.pop(minIndex)
				if node[0] == target:
					return node[1]
				for i in range(0,len(self.edges)):
					if self.edges[i]>0 and (self.getDistanceOfUnvisited(unvisited,i) != -1):
						alt =  node[1] + self.edges[i]
						if alt < self.getDistanceOfUnvisited(unvisited, i):
							self.setDistanceOfUnvisited(unvisited, i, alt)
		
		def setDistanceOfUnvisited(self, unvisited, index, value):
			for element in unvisited:
				if element[0] == index:
					element[1] = value
		
		def getMinFromUnvisited(self, unvisited):
			min = float("inf")
			index = -1
			for i in range(0,len(unvisited)):
				if unvisited[i][1] < min:
					min = unvisited[i][1]
					index = i
			return index
		
		def getDistanceOfUnvisited(self, unvisited, index):
			for element in unvisited:
				if element[0] == index:
					return element[1]
			return -1
			
		
	
			