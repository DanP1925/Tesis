from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from stop_words import get_stop_words
import math

class tfIdf:
	
	def __init__(self, tweets):
		self.termDocument = self.getTermDocumentMatrix(tweets)
		self.tiMatrix = self.obtaintTfIdf()
		
	def getTermDocumentMatrix(self, tweets):
		numTweets = 0
		termList = dict()
		
		for tweet in tweets:
			rawTweet = self.getRawTweet(tweet)
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
	
	def getRawTweet(self, tweet):
		if tweet.text is not None:
			full = tweet.text
		else:
			full = ""
		for sentiment in tweet:
			if sentiment.text is not None:
				full+=sentiment.text
			if sentiment.tail is not None:
				full +=sentiment.tail
		return full
		
	def isValidWord(self,word):
		banned = [ '@','"', ':', ".", ",", "#", "=","http", "\"\"", "?", "-", '``', "\'\'", "...", "!","(",")", "y","q","x","a","Y","X",";", "d"]
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
				
		
	def obtaintTfIdf(self):
		
		matrix = []
		for key in self.termDocument:
			matrix.append(self.termDocument[key])
		
		numTerm = len(matrix)
		numDocs = len(matrix[0])
		
		for j in range(0,numDocs):
			wordTotal = self.wordTotal(matrix, numTerm,j)
			
			for i in range(0,numTerm):
				matrix[i][j] = float(matrix[i][j])
				
				if matrix[i][j] != 0:
					termDocumentOcurrences = self.termDocumentOcurrences(matrix, numDocs, i)
				
					termFrequency = matrix[i][j]/float(wordTotal)
					inverseDocumentFrequency = math.log(math.fabs(numDocs/float(termDocumentOcurrences)))
					
					matrix[i][j] = termFrequency*inverseDocumentFrequency
		
		tiMatrix = dict()
		index = 0
		for key in self.termDocument:
			tiMatrix[key] = matrix[index]
			index+=1
		return tiMatrix

	def wordTotal(self, matrix, numTerm, j):
		sum = 0
		for i in range(0,numTerm):
			if matrix[i][j]>0:
				sum+=1
		return sum
					
	def termDocumentOcurrences(self, matrix, numDocs, i):
		sum = 0
		for j in range(0,numDocs):
			if matrix[i][j]>0:
				sum +=1
		return sum
		
	def printTIMatrix(self):
		for key in self.tiMatrix:
			print(key, ' ')
			print(self.tiMatrix[key])