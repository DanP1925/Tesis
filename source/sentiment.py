class Sentiment:

	def __init__(self, text, aspect, polarity):
		self.text = text
		self.aspect = aspect
		self.polarity = polarity
		
	def termSimilarity(self,target):
		return 1
	
	def polaritySimilarity(self,target):
		return 1
		
	def isEqual(self, newSentiment):
		if self.text == newSentiment.text and self.polarity == newSentiment.polarity:
			return  True
		return False
		
	def similarity(self, target):
		return ((2/3)*self.termSimilarity(target) + (1/3)*self.polaritySimilarity(target))
	
	def debug(self):
		print('Sentiment')
		print(self.text)
		print(self.aspect)
		print(self.polarity)