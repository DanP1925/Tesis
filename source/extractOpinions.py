from xml.etree import cElementTree as ET

def extractEntity(tweet):
	result = []
	for sentiment in tweet:
		entity = sentiment.get('entity')
		if entity not in result:
			result.append(entity)
	return result

def main():
	doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	#doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	tree = ET.parse(doc)
	tweets = tree.getroot()
	entities = dict()
	
	i=1
	for tweet in tweets:
		tweetEntities = extractEntity(tweet)
		
	print(entities)
	
	
if __name__ == "__main__":
	main()