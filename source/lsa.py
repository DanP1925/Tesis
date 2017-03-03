import scipy
import numpy
import math

class LSA:
	
	def __init__(self, corpus, xmlparser):
		self.tDMatrix = corpus.getTermDocumentMatrix(xmlparser)
		self.u = None
		self.sigma = None
		self.vt = None
		self.valueMatrix = None
		
	def pyMatrix(self):
		matrix = []
		for key in self.tDMatrix:
			matrix.append(self.tDMatrix[key])
		return matrix
		
	def singularValueDecomposition(self):
		matrix = self.pyMatrix()
		self.u, self.sigma, self.vt = scipy.linalg.svd(matrix)
		
	def l2norm(self):
		sum = 0
		for elem in self.sigma:
			sum += pow(elem,2)
		return math.sqrt(sum)
		
	def reduceDimension(self):
		numToReduce = math.floor(self.l2norm())
		ascendingList = sorted(list(self.sigma))
		while numToReduce > 0:
			numToReduce -=1
			index = list(self.sigma).index(ascendingList[numToReduce])
			self.sigma[index] = 0
			
	def reconstructMatrix(self):
		self.valueMatrix = numpy.dot(numpy.dot(self.u, scipy.linalg.diagsvd( self.sigma,len(self.tDMatrix),len(self.vt))),self.vt)
		