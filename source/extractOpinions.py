from xml.etree import cElementTree as ET

def extractEntity(tweet):
	result = []
	for sentiment in tweet:
		entity = sentiment.get('entity')
		if entity not in result:
			result.append(entity)
	return result

class Entities:
	entities = dict()
	
	def addNewEntities(self, newEntities):
		for entity in newEntities:
			if entity not in self.entities:
				self.entities[entity] = None
	
	def printEntities(self):
		for key in self.entities:
			print(key)
	
def main():
	doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	#doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	tree = ET.parse(doc)
	tweets = tree.getroot()
	entities = Entities()
	
	i=1
	for tweet in tweets:
		tweetEntities = extractEntity(tweet)
		entities.addNewEntities(tweetEntities)
		i=i+1
	
	entities.printEntities()
	
	
if __name__ == "__main__":
	main()