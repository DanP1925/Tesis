import unittest
import testxmlparser as XML
import testcorpus as corpus

if __name__ == '__main__':
	suiteXml = unittest.TestLoader().loadTestsFromTestCase(XML.extractEntityMethod)
	unittest.TextTestRunner(verbosity=2).run(suiteXml)
	suiteCorpus = unittest.TestLoader().loadTestsFromTestCase(corpus.addNewEntitiesMethod)
	unittest.TextTestRunner(verbosity=2).run(suiteCorpus)