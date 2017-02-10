import xmlparser as XML
import entities as ent

def main():
	doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	#doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	
	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	entities = ent.Entities()
	
	i=1
	for tweet in tweets:
		tweetEntities = xmlparser.extractEntity(tweet)
		entities.addNewEntities(tweetEntities)
		tweetAspects = xmlparser.extractAspects(tweet)
		i=i+1
	
	
if __name__ == "__main__":
	main()