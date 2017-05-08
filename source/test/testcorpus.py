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
	
	def setUp(self):
		self.corpus = COR.Corpus()

	def testAddNewEntitiesSingle(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[0])
		self.corpus.addNewEntities(tweetEntities)
		self.assertEqual(self.corpus.asEntityList(),['Partido_Popular'])
		del self.corpus.entities[:]
		
	def testAddNewEntitiesMultiple(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[1])
		self.corpus.addNewEntities(tweetEntities)
		self.assertEqual(self.corpus.asEntityList(),['Partido_Socialista_Obrero_Espanol', 'Partido_Popular'])
		del self.corpus.entities[:]