import xmlparser as XML
import corpus as COR
import lsa as LAT
import sentiStrength as SENSTR
import time
import sys

DEFAULT_FACTOR = 1.0/3

def initializeFactors():
    if (len(sys.argv)>1):
        positiveFactor = float(sys.argv[1])
        if (len(sys.argv)>2):
            negativeFactor = float(sys.argv[2])
            if (len(sys.argv)>3):
                controversyFactor = float(sys.argv[3])
            else:
                controversyFactor = DEFAULT_FACTOR 
        else:
            negativeFactor = DEFAULT_FACTOR 
            controversyFactor = DEFAULT_FACTOR 
    else:
        positiveFactor = DEFAULT_FACTOR 
        negativeFactor = DEFAULT_FACTOR 
        controversyFactor = DEFAULT_FACTOR 

    return positiveFactor, negativeFactor, controversyFactor


def main():

    #doc = "/home/daniel/data/Ciclo6/Tesis2/stompol-tweets-train-tagged.xml"
    doc = "/home/daniel/data/Cato/Ciclo6/Tesis2/xmlSampleFile.xml"
    #doc = "/home/daniel/data/Ciclo6/Tesis2/xmlSampleFile2.xml"
    #doc = "/home/daniel/data/Ciclo6/Tesis2/xmlStandardFile.xml"

    positiveFactor, negativeFactor, controversyFactor = initializeFactors() 

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
