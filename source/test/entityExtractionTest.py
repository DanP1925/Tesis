import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
import xmlparser as XML
import entities as ENT

class EntityExtractionMethod(unittest.TestCase):
	
	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"

	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	entities = ENT.Entities()
	
	def testEntityExtractionSingle(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[0]),['Partido_Popular'])
		
	def testEntityExtractionMultiple(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[1]),['Partido_Socialista_Obrero_Espanol','Partido_Popular'])
	
	def testEntityExtractionMultipleOnOneEntity(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[2]),['Partido_Popular','Podemos','Partido_Socialista_Obrero_Espanol','Izquierda_Unida','Ciudadanos'])
	
	def testAddNewEntitiesSingle(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[0])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':None})
		self.entities.entities.clear()
		
	def testAddNewEntitiesMultiple(self):
		tweetEntities = self.xmlparser.extractEntity(self.tweets[1])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':None, 'Partido_Socialista_Obrero_Espanol':None})
		self.entities.entities.clear()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(EntityExtractionMethod)
	unittest.TextTestRunner(verbosity=2).run(suite)