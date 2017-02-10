import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
import xmlparser as XML

class extractEntityMethod(unittest.TestCase):
	
	doc = r"D:\Ciclo 6\Tesis 2\Tesis\source\test\xmltestfile.xml"

	xmlparser = XML.XmlParser(doc)
	tweets = xmlparser.root
	
	def testEntityExtractionSingle(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[0]),['Partido_Popular'])
		
	def testEntityExtractionMultiple(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[1]),['Partido_Socialista_Obrero_Espanol','Partido_Popular'])
	
	def testEntityExtractionMultipleOnOneEntity(self):
		self.assertEqual(self.xmlparser.extractEntity(self.tweets[2]),['Partido_Popular','Podemos','Partido_Socialista_Obrero_Espanol','Izquierda_Unida','Ciudadanos'])