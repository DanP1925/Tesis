import xmlparser as XML
import corpus as COR
import sentiment as SEN
import lsa as LAT

def main():
	#doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	
	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	corpus = COR.Corpus()
	
	for tweet in tweets:
		tweetEntities = xmlparser.extractEntity(tweet)
		corpus.addNewEntities(tweetEntities)
		for tweetEntity in tweetEntities:
			entity = corpus.getEntity(tweetEntity)
			entity.addReview()
			for sentiment in tweet:
				entity.addSentiment(SEN.Sentiment(sentiment.text, sentiment.get('aspect'), sentiment.get('polarity')))					
	
	lsa  = LAT.LSA(corpus, xmlparser)
	lsa.tfidf()
	lsa.singularValueDecomposition()
	lsa.reduceDimension()
	lsa.reconstructMatrix()
	
	for entity in corpus.entities:
		entity.generateGraph(lsa)
		entity.initializeLeaders()
		# entity.printMatrix()
		print()
	
	
if __name__ == "__main__":
	main()