class structureItem:
	
	def __init__(self, aspect):
		self.aspect = aspect
		self.representative = -1
		self.opposite = None
		self.support = None
		self.relPositiveFreq = 0
		self.relNegativeFreq = 0
		self.absPositiveFreq = 0
		self.absNegativeFreq = 0

	def getLeaderRepresentative(self, communities, graph):
		max = -1
		representative = -1
		for community in communities:
			aspect = graph.nodes[community.leader].sentiment.aspect
			if aspect == self.aspect:
				if graph.nodes[community.leader].score > max:
					max = graph.nodes[community.leader].score 
					representative = community.leader
		self.representative =  representative

	def getRepresentative(self, nodes):
		max = -1
		representative = -1
		for i in range(0,len(nodes)):
			aspect = nodes[i].sentiment.aspect
			if aspect == self.aspect:
				score = nodes[i].score
				if score > max:
					max = score
					representative = i
		self.representative = representative

	def getFrequencies(self, nodes):
		positive = 0
		negative = 0
		total = 0
		for node in nodes:
			if node.sentiment.aspect == self.aspect:
				if node.sentiment.polarity == 'P':
					positive += 1
				elif node.sentiment.polarity == 'N':
					negative += 1
				total +=1
		self.absPositiveFreq = positive
		self.absNegativeFreq = negative 
		self.relPositiveFreq = positive/total
		self.relNegativeFreq = negative/total

	def getOppositeOpinion(self, nodes):
		max = -1
		opposite = -1
		for i in range(0, len(nodes)):
			aspect = nodes[i].sentiment.aspect
			if aspect == self.aspect:
				selfPolarity = nodes[self.representative].sentiment.polarity 
				targetPolarity = nodes[i].sentiment.polarity	
				if self.isOppositePolarity(selfPolarity, targetPolarity):
					score = nodes[i].score
					if score > max:
						max = score
						opposite = i
		if opposite != -1:
			self.opposite = i

	def isOppositePolarity(self, selfPolarity, targetPolarity):
		if selfPolarity == 'P':
			if targetPolarity == 'N':
				return True
		elif selfPolarity == 'N':
			if targetPolarity == 'P':
				return True 
		return False

	def getSupportiveOpinion(self, nodes):
		return 0
		#max = -1
		#opoosite = -1
		#for node in nodes:

	def printItem(self, nodes):
		print(self.aspect)
		print(str(self.representative) + ': ' + nodes[self.representative].sentiment.text)
		if self.opposite is not None:
			print(str(self.opposite) + ': ' + nodes[self.opposite].sentiment.text)
		if self.support is not None:
			print(str(self.support) + ': ' + nodes[self.support].sentiment.text)
		print('Relative frequencies: ' + str(self.relPositiveFreq)  + ' ' + str(self.relNegativeFreq))
		print('Absolute frequencies: ' + str(self.absPositiveFreq)  + ' ' + str(self.absNegativeFreq))
		print('-----------------------------')
	
