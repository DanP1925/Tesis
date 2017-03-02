class LSA:
	
	def __init__(self, corpus, xmlparser):
		self.tDMatrix = corpus.getTermDocumentMatrix( xmlparser)