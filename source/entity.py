class Entity:

	def __init__(self, name):
		self.name = name
		self.sentiments = []
		
	def addSentiment(self, newSentiment):
		self.sentiments.append(newSentiment)
	
	def debug(self):
		print('Entity')
		print(self.name)
		for sentiment in self.sentiments:
			sentiment.debug()