import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
import xmlparser as XML
import corpus as COR

class addNewEntitiesMethod(unittest.TestCase):

	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"

	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root

	def testAddNewEntitiesSingle(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[0])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':[[],[]]})
		self.entities.entities.clear()
		
	def testAddNewEntitiesMultiple(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[1])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':[[],[]], 'Partido_Socialista_Obrero_Espanol':[[],[]]})
		self.entities.entities.clear()