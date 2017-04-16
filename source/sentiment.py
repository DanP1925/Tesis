import corpus as COR
import math
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from stop_words import get_stop_words
from scipy.stats import spearmanr

class Sentiment:

	def __init__(self, text, aspect, polarity):
		self.text = text
		self.aspect = aspect
		self.polarity = polarity
		self.vectorRepresentation = []
		self.polarityStrength = []
		
	def termSimilarity(self, target):
		if len(self.vectorRepresentation) == 0 or len(target.vectorRepresentation) == 0:
			return 0
		
		n1 = 0
		sum1 = 0
		for vector in self.vectorRepresentation:
			n2 = 0
			sum2 = 0
			for vector2 in target.vectorRepresentation:
				sum2 += spearmanr(vector[1],vector2[1])[0]
				n2 += 1
			if n2 != 0:
				sum1 += sum2/n2
				n1 += 1
		
		if n1 == 0:
			return 0
		return sum1/n1
	
	def polaritySimilarity(self, target):
		x = self.polarityStrength[0] - target.polarityStrength[0]
		y = self.polarityStrength[1] - target.polarityStrength[1]
		return math.sqrt(pow(x,2) + pow(y,2))
		
	def similarity(self, target):
		mints = -1
		maxts = 1
		minps = 0
		maxps =  math.sqrt(pow(4,2) + pow(4,2))
		ts = self.termSimilarity(target)
		ps = maxps - self.polaritySimilarity(target)
		newts = ((ts - mints)/(maxts - mints))
		newps = ((ps - minps)/(maxps - minps))
		return ((2/3)*newts + (1/3)*newps)
		
	def isEqual(self, newSentiment):
		if self.text == newSentiment.text and self.polarity == newSentiment.polarity:
			return  True
		return False
	
	def debug(self):
		print('Sentiment')
		print(self.text)
		print(self.aspect)
		print(self.polarity)