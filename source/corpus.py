import entity as ENT
from nltk import word_tokenize

class Corpus:
	
	def __init__(self):
		self.entities = []
	
	def addNewEntities(self, newEntities):
		for newEntity in newEntities:
			if not self.isInEntities(newEntity):
				self.entities.append(ENT.Entity(newEntity))
				
	def isInEntities(self, value):
		for entity in self.entities:
			if entity.name == value:
				return True
		return False
				
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
	
	def debug(self):
		for entity in self.entities:
			entity.debug()
			print()
			
	def assignSemanticSimilarity(self, lsa):
		for entity in self.entities:
			for review in entity.reviews:
				for sentiment in review.sentiments:
					wordList = word_tokenize(sentiment.text)
					for word in wordList:
						if lsa.tfIdf.isValidWord(word):
							term = lsa.tfIdf.cleanWord(word)
							vector = lsa.getVector(term)
							if len(vector) !=0:
								sentiment.vectorRepresentation.append((term,vector))