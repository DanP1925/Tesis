import scipy

class LSA:
	
	def __init__(self, corpus, xmlparser):
		self.tDMatrix = corpus.getTermDocumentMatrix(xmlparser)
		
	def pyMatrix(self):
		matrix = []
		for key in self.tDMatrix:
			matrix.append(self.tDMatrix[key])
		return matrix
		
	def singularValueDecomposition(self):
		matrix = self.pyMatrix()
		u, sigma, vt = scipy.linalg.svd(matrix)
		