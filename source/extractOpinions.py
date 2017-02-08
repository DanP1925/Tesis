from xml.etree import cElementTree as ET

def extractEntity(tweet)
	for sentiments in tweet:
		sentiment.get('entity')

def main():
	doc = "D:\Ciclo 6\Tesis 2\stompol-tweets-train-tagged.xml"
	tree = ET.parse(doc)
	tweets = tree.getroot()
	i=1
	for tweet in tweets:
		entities = extractEntity(tweet)
	
	
if __name__ == "__main__":
	main()