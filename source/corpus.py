import entity as ENT
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from stop_words import get_stop_words

class Corpus:
	
	def __init__(self):
		self.entities = []
	
	def isInEntities(self, value):
		for entity in self.entities:
			if entity.name == value:
				return True
		return False
	
	def addNewEntities(self, newEntities):
		for newEntity in newEntities:
			if not self.isInEntities(newEntity):
				self.entities.append(ENT.Entity(newEntity))
				
	def asEntityList(self):
		result = []
		for entity in self.entities:
			result.append(entity.name)
		return result
		
	def getEntity(self, value):
		for entity in self.entities:
			if entity.name == value:
				return entity
		return None
		
	def isValidWord(self,word):
		banned = [ '@','"', ':', ".", ",", "#", "http", "\"\"", "?", "-", '``', "\'\'", "...", "!","(",")", "y","q","x","a","Y","X",";", "d"]
		stopwords = get_stop_words('spanish')
		if not word in stopwords and not word in banned:
			if not(word[0]=="/" and word[1]=="/"):
				return True
		return False
	
	def cleanWord(self, word):
		stemmer = SnowballStemmer('spanish')
		term = stemmer.stem(word)
		if term[0] == "¿":
			term = term[1:]
		if term:
			if term[-1] == "_":
				term = term[:-1]
		return term
	
	def getTermDocumentMatrix(self, xmlparser):
		tweets = xmlparser.root
		numTweets = 0
		termList = dict()
		
		for tweet in tweets:
			rawTweet = xmlparser.reestructure(tweet)
			wordList = word_tokenize(rawTweet)
			for word in wordList:
				if self.isValidWord(word):
					term = self.cleanWord(word)
					if term not in termList:
						newList = [0] * numTweets
						newList.append(1)
						termList[term] = newList
					else:
						if len(termList[term])==numTweets+1:
							termList[term][-1] +=1
						else:
							termList[term].append(1)
			numTweets +=1
			for key in termList:
				if len(termList[key])<numTweets:
					termList[key].append(0)
		return termList
	
	def debug(self):
		for entity in self.entities:
			entity.debug()
			print()