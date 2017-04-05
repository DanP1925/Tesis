import xmlparser as XML
import corpus as COR
import lsa as LAT

def main():
	#doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	doc = r"D:\Ciclo 6\Tesis 2\xmlSamplefile.xml"
	
	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	corpus = COR.Corpus()
	
	for tweet in tweets:
		tweetEntities = xmlparser.extractEntity(tweet)
		corpus.addNewEntities(tweetEntities)
		for tweetEntity in tweetEntities:
			entity = corpus.getEntity(tweetEntity)
			entity.addReview(tweet)
			
	lsa  = LAT.LSA(tweets)
	lsa.singularValueDecomposition()
	lsa.reduceDimension()
	lsa.reconstructMatrix()
	corpus.assignSemanticSimilarity(lsa)
	
	# for entity in corpus.entities:
		# entity.obtainLeaders()
		# entity.generateGraph(lsa)
		# entity.initializeLeaders()
		# previousLeaders = list(entity.leaders)
		# distances = entity.getDistances()
		# print()
	
if __name__ == "__main__":
	main()