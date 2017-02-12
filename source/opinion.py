class Opinion:
	
	def __init__(self, opinion):
		self.opinion = opinion
		self.phrases = []
		
	def debug(self):
		print('Opinion')
		print(self.opinion)
		for phrase in self.phrases:
			print('Phrase')
			print(phrase)
			