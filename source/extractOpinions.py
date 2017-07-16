import xmlparser as XML
import corpus as COR
import lsa as LAT
import sentiStrength as SENSTR
import time
import sys

def main():
    #doc = "/home/daniel/data/Ciclo6/Tesis2/stompol-tweets-train-tagged.xml"
    doc = "/home/daniel/data/Ciclo6/Tesis2/xmlSampleFile.xml"
    #doc = "/home/daniel/data/Ciclo6/Tesis2/xmlSampleFile2.xml"
    #doc = "/home/daniel/data/Ciclo6/Tesis2/xmlStandardFile.xml"
	
    if (len(sys.argv)>1):
        positiveFactor = float(sys.argv[1])
        if (len(sys.argv)>2):
            negativeFactor = float(sys.argv[2])
            if (len(sys.argv)>3):
                controversyFactor = float(sys.argv[3])
            else:
                controversyFactor = 1.0/3
        else:
            negativeFactor = 1.0/3
            controversyFactor = 1.0/3
    else:
        positiveFactor = 1.0/3
        negativeFactor = 1.0/3
        controversyFactor = 1.0/3
    
    print(positiveFactor)
    print(negativeFactor)
    print(controversyFactor)

    xmlparser = XML.XmlParser(doc)
    tweets = xmlparser.root
    corpus = COR.Corpus(positiveFactor, negativeFactor, controversyFactor)

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
        print(entity.reestructure(entity.generateSummary(), 1200))
        print()

if __name__ == "__main__":
    main()
