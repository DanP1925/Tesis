from xml.etree import cElementTree as ET

class XmlParser:

	def __init__(self, doc):
		self.tree = ET.parse(doc)
		self.root = self.tree.getroot()

	def extractEntity(self,tweet):
		result = []
		for sentiment in tweet:
			entity = sentiment.get('entity')
			if entity.find('|'):
				entities = entity.split('|')
				for subentity in entities:
					if subentity not in result:
						result.append(subentity)
			else:
				if entity not in result:
					result.append(entity)
		return result
		
	def extractAspects(self,tweet, targetEntity):
		result = []
		for sentiment in tweet:
			entity = sentiment.get('entity')
			if entity.find('|'):
				entities = entity.split('|')
				for subentity in entities:
					if subentity == targetEntity:
						aspect = sentiment.get('aspect')
						if aspect not in result:
							result.append(aspect)
			else:
				if entity == targetEntity:
					aspect = sentiment.get('aspect')
					if aspect not in result:
							result.append(aspect)
		return result