import scipy
import numpy
import math

class LSA:
	
	def __init__(self, corpus, xmlparser):
		self.tDMatrix = corpus.getTermDocumentMatrix(xmlparser)
		self.tfidfMatrix = self.pyMatrix()
		self.u = None
		self.sigma = None
		self.vt = None
		self.valueMatrix = None
	
	def pyMatrix(self):
		matrix = []
		for key in self.tDMatrix:
			matrix.append(self.tDMatrix[key])
		return matrix
	
	def wordTotal(self, numTerm, j):
		sum = 0
		for i in range(0,numTerm):
			if self.tfidfMatrix[i][j]>0:
				sum+=1
		return sum
	
	def termDocumentOcurrences(self, numDocs, i):
		sum = 0
		for j in range(0,numDocs):
			if self.tfidfMatrix[i][j]>0:
				sum +=1
		return sum
	
	def tfidf(self):
		numTerm = len(self.tfidfMatrix)
		numDocs = len(self.tfidfMatrix[0])
		
		for j in range(0,numDocs):
			wordTotal = self.wordTotal(numTerm,j)
			for i in range(0,numTerm):
				self.tfidfMatrix[i][j] = float(self.tfidfMatrix[i][j])
				if self.tfidfMatrix[i][j] != 0:
					
					termDocumentOcurrences = self.termDocumentOcurrences(numDocs, i)
				
					termFrequency = self.tfidfMatrix[i][j]/float(wordTotal)
					inverseDocumentFrequency = math.log(math.fabs(numDocs/float(termDocumentOcurrences)))
					
					self.tfidfMatrix[i][j] = termFrequency*inverseDocumentFrequency
	
	def singularValueDecomposition(self):
		self.u, self.sigma, self.vt = scipy.linalg.svd(self.tfidfMatrix)
		
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
		