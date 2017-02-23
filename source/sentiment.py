class Sentiment:

	def __init__(self, text, aspect, polarity):
		self.text = text
		self.aspect = aspect
		self.polarity = polarity
		
	def debug(self):
		print('Sentiment')
		print(self.text)
		print(self.aspect)
		print(self.polarity)