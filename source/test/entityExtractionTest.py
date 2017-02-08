import unittest
from xml.etree import cElementTree as ET

class EntityExtractionMethod(unittest.TestCase):
	
	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"
	tree = ET.parse(doc)
	tweets = tree.getroot()
	
	def testSingleEntityExtraction(self):
		self.assertEqual(extractEntity(tweets[0]),['Partido_Popular'])
		
	def testMultipleEntityExtraction(self):
		self.assertEqual(extractEntity(tweets[1]),['Partido_Socialista_Obrero_Espanol','Partido_Popular'])

if __name__ == '__main__':
	unittest.main()