class Entity:

	def __init__(self, name):
		self.name = name
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
			
	def generateGraph(self):
		for i in range(0,len(self.sentiments)):
			list = []
			for j in range(0,len(self.sentiments)):
				list.append(self.sentiments[i].similarity(self.sentiments[j]))
			self.matrix.append(list)
			
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