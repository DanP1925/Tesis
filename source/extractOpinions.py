import xmlparser as XML
import corpus as COR
import lsa as LAT
import sentiStrength as SENSTR
import time

def main():
	#doc = "/home/daniel/data/Ciclo6/Tesis2/stompol-tweets-train-tagged.xml"
	doc = "/home/daniel/data/Ciclo6/Tesis2/xmlSampleFile.xml"
	#doc = "/home/daniel/data/Ciclo6/Tesis2/xmlSampleFile2.xml"
	#doc = "/home/daniel/data/Ciclo6/Tesis2/xmlStandardFile.xml"
	
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
	
	sentiStrength = SENSTR.sentiStrength()
	corpus.assignPolaritySimilarity(sentiStrength)
	
	for entity in corpus.entities:
		entity.obtainLeaders()
		entity.obtainCommunities()
		entity.assignOrder()
		entity.fullParsing()
		print(entity.generateSummary())
		print()

if __name__ == "__main__":
	main()
