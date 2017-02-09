import unittest
from xml.etree import cElementTree as ET
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
import extractOpinions as EO

class EntityExtractionMethod(unittest.TestCase):
	
	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	tree = ET.parse(doc)
	tweets = tree.getroot()
	entities = EO.Entities()
	
	def testEntityExtractionSingle(self):
		self.assertEqual(EO.extractEntity(self.tweets[0]),['Partido_Popular'])
		
	def testEntityExtractionMultiple(self):
		self.assertEqual(EO.extractEntity(self.tweets[1]),['Partido_Socialista_Obrero_Espanol','Partido_Popular'])
		
	def testAddNewEntitiesSingle(self):
		tweetEntities = EO.extractEntity(self.tweets[0])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':None})
		self.entities.entities.clear()
		
	def testAddNewEntitiesMultiple(self):
		tweetEntities = EO.extractEntity(self.tweets[1])
		self.entities.addNewEntities(tweetEntities)
		self.assertEqual(self.entities.entities,{'Partido_Popular':None, 'Partido_Socialista_Obrero_Espanol':None})
		self.entities.entities.clear()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(EntityExtractionMethod)
	unittest.TextTestRunner(verbosity=2).run(suite)