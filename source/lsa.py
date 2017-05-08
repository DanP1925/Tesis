import tfIdf as TI
import scipy
import numpy
import math

class LSA:
	
	def __init__(self, tweets):
		self.tfIdf = TI.tfIdf(tweets)
		self.tfIdfMatrix = self.tfIdf.tiMatrix
		self.u = None
		self.sigma = None
		self.vt = None
		self.valueMatrix = None
	
	def singularValueDecomposition(self):
		matrix = []
		for key in self.tfIdfMatrix:
			matrix.append(self.tfIdfMatrix[key])
		self.u, self.sigma, self.vt = scipy.linalg.svd(matrix)
		
	def reduceDimension(self):
		numToReduce = math.floor(self.l2norm())
		ascendingList = sorted(list(self.sigma))
		while numToReduce > 0:
			numToReduce -=1
			index = list(self.sigma).index(ascendingList[numToReduce])
			self.sigma[index] = 0
			
	def l2norm(self):
		sum = 0
		for elem in self.sigma:
			sum += pow(elem,2)
		return math.sqrt(sum)
			
	def reconstructMatrix(self):
		reconstructedMatrix = numpy.dot(numpy.dot(self.u, scipy.linalg.diagsvd( self.sigma,len(self.tfIdfMatrix),len(self.vt))),self.vt)
		valueMatrix = dict()
		index = 0
		for key in self.tfIdfMatrix:
			valueMatrix[key] = reconstructedMatrix[index]
			index += 1
		self.valueMatrix = valueMatrix
		
	def isInTDMatrix(self, target):
		for key in self.tDMatrix:
			if target == key:
				return True
		return False
	
	def getVector(self, target):
		for key in self.valueMatrix:
			if target == key:
				return self.valueMatrix[key]
		return []
	
	def printvalueMatrix(self):
		for key in self.valueMatrix:
			print(key, ' ')
			print(self.valueMatrix[key])
				