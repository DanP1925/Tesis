import entity as ENT
from nltk import word_tokenize

class Corpus:
	
    def __init__(self, positiveFactor, negativeFactor, controversyFactor):
        self.entities = []
        self.positiveFactor = positiveFactor
        self.negativeFactor = negativeFactor
        self.controversyFactor = controversyFactor
	
    def addNewEntities(self, newEntities):
        for newEntity in newEntities:
            if not self.isInEntities(newEntity):
                self.entities.append(ENT.Entity(newEntity, self.positiveFactor, self.negativeFactor, self.controversyFactor))
				
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
								
    def assignPolaritySimilarity(self, sentiStrength):
        for entity in self.entities:
            for review in entity.reviews:
                for sentiment in review.sentiments:
                    polarity = sentiStrength.getDefaultPolarity(sentiment.polarity)
					
                    wordList = word_tokenize(sentiment.text)
                    maxGood = 0
                    maxBad = 0
                    hasBoostingWord = False
                    boostingValue = 0
                    for word in wordList:
                        if sentiStrength.isSentimentWord(word):
                            value = sentiStrength.getSentimentValue(word)
                            if hasBoostingWord:
                                value = value + boostingValue
                                hasBoostingWord = False
                                boostingValue = 0
                            if value > 0:
                                if value > maxGood:
                                    maxGood = value
                            elif value < 0:
                                if value < maxBad:
                                    maxBad = value
                        elif sentiStrength.isNegatingWord(word):
                            break
                        elif sentiStrength.isBoostingWord(word):
                            hasBoostingWord = True
                            boostingValue = sentiStrength.getBoostingValue(word)
                    polarityStrength = [polarity[0],polarity[1]]
                    if maxGood !=0:
                        polarityStrength[0] = maxGood
                    if maxBad != 0:
                        polarityStrength[1] = maxBad
                    sentiment.polarityStrength = polarityStrength
							
    def debug(self):
        for entity in self.entities:
            entity.debug()
            print()
