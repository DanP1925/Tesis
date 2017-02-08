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
	
	def testSingleEntityExtraction(self):
		self.assertEqual(EO.extractEntity(self.tweets[0]),['Partido_Popular'])
		
	def testMultipleEntityExtraction(self):
		self.assertEqual(EO.extractEntity(self.tweets[1]),['Partido_Socialista_Obrero_Espanol','Partido_Popular'])

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(EntityExtractionMethod)
	unittest.TextTestRunner(verbosity=2).run(suite)