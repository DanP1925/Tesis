import xmlparser as XML
import corpus as COR

def main():
	doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	#doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	
	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	corpus = COR.Corpus()
	
	i=1
	for tweet in tweets:
		tweetEntities = xmlparser.extractEntity(tweet)
		corpus.addNewEntities(tweetEntities)
		for tweetEntity in tweetEntities:
			tweetAspects = xmlparser.extractAspects(tweet,tweetEntity)
			entity = corpus.getEntity(tweetEntity)
			entity.addNewAspects(tweetAspects)
			
		i=i+1
	
if __name__ == "__main__":
	main()