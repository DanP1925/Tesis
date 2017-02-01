from xml.etree import cElementTree as ET

def main():
	doc = "stompol-tweets-train-tagged.xml"
	
	words = obtainWords(doc)
	clusters = clustering(words)
	display(clusters)

def obtainWords(doc):
	words = []
	return words
	
def clustering(words):
	return words
	
def display(clusters):
	print (clusters)
	
if __name__ == "__main__":
	main()