from difflib import SequenceMatcher
class sentiStrength:

	def __init__(self):
		wordListDoc = "/home/daniel/data/Ciclo 6/Tesis 2/dictionary/sentiment_words_spanish.txt"
		boosterDoc = "/home/daniel/data/Ciclo 6/Tesis 2/dictionary/booster_words_spanish.txt"
		negationDoc =  "/home/daniel/data/Ciclo 6/Tesis 2/dictionary/negating_words_spanish.txt"
		self.sentimentWordList = self.parseDictionary(wordListDoc)
		self.wordBoosterList = self.parseDictionary(boosterDoc)
		self.wordNegationList = self.parseNegationDictionary(negationDoc)
		
	def parseDictionary(self, filename):
		dictionary = dict()
		
		file = open(filename, 'r')
		for line in file:
			words = line.split()
			word = words[0]
			value = int(words[2])
			dictionary[word] = value
		file.close()
		return dictionary
		
	def parseNegationDictionary(self, filename):
		dictionary = []
		
		file = open(filename, 'r')
		for line in file:
			words = line.split()
			dictionary.append(words[0])
		file.close()
		return dictionary
	
	def getDefaultPolarity(self, polarity):
		if polarity == "P":
			return (5,-1)
		elif polarity == "N":
			return (1,-5)
		else:
			return (1,-1)
			
	def isSentimentWord(self, target):
		for key in self.sentimentWordList:
			if '#' in key:
				if SequenceMatcher(None, target, key).ratio() > 0.7:
					return True
			elif key == target:
					return True
		return False
		
	def getSentimentValue(self, target):
		for key in self.sentimentWordList:
			if '#' in key:
				if SequenceMatcher(None, target, key).ratio() > 0.7:
					return self.sentimentWordList[key]
			elif key == target:
					return self.sentimentWordList[key]
		
			
	def isNegatingWord(self, target):
		if target in self.wordNegationList:
			return True
		return False
			
	def isBoostingWord(self, target):
		for key in self.wordBoosterList:
			if '#' in key:
				if SequenceMatcher(None, target, key).ratio() > 0.7:
					return True
			elif key == target:
					return True
		return False
		
	def getBoostingValue(self, target):
		for key in self.wordBoosterList:
			if '#' in key:
				if SequenceMatcher(None, target, key).ratio() > 0.7:
					return self.wordBoosterList[key]
			elif key == target:
					return self.wordBoosterList[key]
