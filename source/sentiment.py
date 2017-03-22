import corpus as COR
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from stop_words import get_stop_words
from scipy.stats import spearmanr

class Sentiment:

	def __init__(self, text, aspect, polarity):
		self.text = text
		self.aspect = aspect
		self.polarity = polarity
		self.degree = 0
		
	def termSimilarity(self, target, lsa):
		sum1 = float(0)
		n1 = 0
		
		corpus = COR.Corpus()
		
		sentence1 = word_tokenize(self.text)
		sentence2 = word_tokenize(target.text)

		for word1 in sentence1:
			sum2 = float(0)
			n2 = 0
			if corpus.isValidWord(word1):
				cleanWord1= corpus.cleanWord(word1)
				if lsa.isInTDMatrix(cleanWord1):
					for word2 in sentence2:
						if corpus.isValidWord(word2):
							cleanWord2 = corpus.cleanWord(word2)
							if lsa.isInTDMatrix(cleanWord2):
								sum2 += spearmanr(lsa.getvector(cleanWord1),lsa.getvector(cleanWord2))[0]
								n2 += 1
					if sum2 >0:
						n1 += 1
						sum1 += sum2/n2
		
		if n1 == 0:
			return -1
			
		return sum1/n1
	
	def polaritySimilarity(self, target):
		if self.polarity == target.polarity:
			return 1
		else:
			return 0
		
	def isEqual(self, newSentiment):
		if self.text == newSentiment.text and self.polarity == newSentiment.polarity:
			return  True
		return False
		
	def similarity(self, target, lsa):
		return ((2/3)*self.termSimilarity(target, lsa) + (1/3)*self.polaritySimilarity(target))
		
	def calculateDegree(self, list):
		degree = 0
		for element in list:
			if element !=0:
				degree +=1
		self.degree = degree
	
	def debug(self):
		print('Sentiment')
		print(self.text)
		print(self.aspect)
		print(self.polarity)