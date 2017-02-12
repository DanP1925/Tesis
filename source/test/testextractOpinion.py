import unittest
import testxmlparser as XML
import testcorpus as corpus

if __name__ == '__main__':
	suiteXmlExtractEntity = unittest.TestLoader().loadTestsFromTestCase(XML.extractEntityMethod)
	suiteXmlExtractAspect = unittest.TestLoader().loadTestsFromTestCase(XML.extractAspectMethod)
	suiteCorpus = unittest.TestLoader().loadTestsFromTestCase(corpus.addNewEntitiesMethod)
	
	suiteList = []
	suiteList.append(suiteXmlExtractEntity)
	suiteList.append(suiteXmlExtractAspect)
	suiteList.append(suiteCorpus)
	
	comboSuite = unittest.TestSuite(suiteList)
	
	unittest.TextTestRunner(verbosity=2).run(comboSuite)