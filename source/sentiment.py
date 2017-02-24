class Sentiment:

	def __init__(self, text, aspect, polarity):
		self.text = text
		self.aspect = aspect
		self.polarity = polarity
		
	def termSimilarity(self,target):
		if self.aspect == target.aspect:
			return 1
		else:
			return 0
	
	def polaritySimilarity(self,target):
		if self.polarity == target.polarity:
			return 1
		else:
			return 0
		
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