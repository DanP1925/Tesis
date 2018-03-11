#! /usr/bin/python3

### REQUIRES python 3 !!!!

## Run:  ./sample.py
## Reads from stdin and writes to stdout
## For example:
##     ./sample.py <test.txt >test_out.txt

import freeling
import sys

class freelingLibrary:


	## ------------  output a parse tree ------------
	def printTree(self, ptree, depth):
	
                node = ptree.begin();
            
                print(''.rjust(depth*2),end='');
                info = node.get_info();
                if (info.is_head()): print('+',end='');
            
                nch = node.num_children();
                if (nch == 0) :
                        w = info.get_word();
                        #print ('({0} {1} {2})'.format(w.get_form(), w.get_lemma(), w.get_tag()),end='');
                        print ('({0})'.format(w.get_form()),end='');
            
                else :
                        print('{0}_['.format(info.get_label()));
                
                        for i in range(nch) :
                                child = node.nth_child_ref(i);
                                self.printTree(child, depth+1);
                
                        print(''.rjust(depth*2),end='');
                        print(']',end='');
                    
                print('');


	def fullParsing(self, text, sentimentText):
	
		## Modify this line to be your FreeLing installation directory
		FREELINGDIR = "/usr/local";
		
		DATA = FREELINGDIR+"/share/freeling/";
		LANG="es";
		
		freeling.util_init_locale("default");
		
		# create language analyzer
		la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");
		
		# create options set for maco analyzer. Default values are Ok, except for data files.
		op= freeling.maco_options("es");
		op.set_data_files( "", 
		                   DATA + "common/punct.dat",
		                   DATA + LANG + "/dicc.src",
		                   DATA + LANG + "/afixos.dat",
		                   "",
		                   DATA + LANG + "/locucions.dat", 
		                   DATA + LANG + "/np.dat",
		                   DATA + LANG + "/quantities.dat",
		                   DATA + LANG + "/probabilitats.dat");
		
		# create analyzers
		tk=freeling.tokenizer(DATA+LANG+"/tokenizer.dat");
		sp=freeling.splitter(DATA+LANG+"/splitter.dat");
		sid=sp.open_session();
		mf=freeling.maco(op);
		
		# activate mmorpho odules to be used in next call
		mf.set_active_options(False, True, True, True,  # select which among created 
		                      True, True, False, True,  # submodules are to be used. 
		                      True, True, True, True ); # default: all created submodules are used
		
		# create tagger, sense anotator, and parsers
		tg=freeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
		sen=freeling.senses(DATA+LANG+"/senses.dat");
		parser= freeling.chart_parser(DATA+LANG+"/chunker/grammar-chunk.dat");
		dep=freeling.dep_txala(DATA+LANG+"/dep_txala/dependences.dat", parser.get_start_symbol());
		
		#split Target as a list
		sentimentText += '.'
		if sentimentText[0] == '@':
			sentimentText = sentimentText[1:]
		target = tk.tokenize(sentimentText)
		targets = sp.split(sid,target,True)
		targets = mf.analyze(targets)
		targets = parser.analyze(targets)
		targets = dep.analyze(targets)

		for s in targets:
			targetr = s.get_parse_tree()
			targetList = self.getTreeAsList(targetr, 0)
			del targetList[-1]

		# process input text
		lin = text
		if lin[0] == '@':
			lin = lin[1:]
		
		#while (lin) :
		        
		l = tk.tokenize(lin);
		ls = sp.split(sid,l,True);
		
		ls = mf.analyze(ls);
		ls = parser.analyze(ls);
		ls = dep.analyze(ls);
		
		finalType = None
		finalList = None
		finalTag = None
		
		## output results
		for s in ls :
			tr = s.get_parse_tree();
			# self.printTree(tr,0);
			wordType, wordList, wordTag = self.getTypeNode(tr, 0, targetList)
			if finalType is None:
				if wordType is not None:
					finalType = wordType 
					finalList = wordList
					finalTag = wordTag
		# clean up       
		sp.close_session(sid);

		return finalType, finalList, finalTag
    
	def getTreeAsList(self, ptree, depth):
		
		node = ptree.begin()
		info = node.get_info()

		nch = node.num_children()
		if (nch == 0):
			w = info.get_word()
			return [w.get_form()]
		else:
			newList = []
			for i in range(nch):
				child = node.nth_child_ref(i)
				newList += self.getTreeAsList(child, depth+1)
		return newList	

	def getTreeAsTagList(self, ptree, depth):
		
		node = ptree.begin()
		info = node.get_info()

		nch = node.num_children()
		if (nch == 0):
			w = info.get_word()
			return [w.get_tag()]
		else:
			newList = []
			for i in range(nch):
				child = node.nth_child_ref(i)
				newList += self.getTreeAsTagList(child, depth+1)
		return newList	

	def getTypeNode(self, ptree, depth, targetList):
		
		node = ptree.begin()
		info = node.get_info();
		
		nch = node.num_children();
		if (nch == 0) :
			return None, None, None
		else:
			wordType = None 
			wordList = None 
			wordTag = None

			newType = info.get_label()
			newList = self.getTreeAsList(ptree,0)
			newTag = self.getTreeAsTagList(ptree, 0)

			if newType == 'sn' or newType == 'grup-verb' or newType == 'grup-verb-inf' or newType == 'grup-sp-inf' or newType == 'grup-sp':
				if self.compareLists(targetList, newList):
					if wordList is None and newList is not None:
							wordType = newType
							wordList = newList
							wordTag = newTag
			for i in range(nch) :
				child = node.nth_child_ref(i);
				sonType, sonList, sonTag = self.getTypeNode(child, depth+1, targetList)
				if sonList is not None:
					if wordList is not None:
						if len(wordList) > len(sonList):
							wordType = sonType
							wordList = sonList
							wordTag = sonTag
					else:
						wordType = sonType
						wordList = sonList
						wordTag = sonTag
			return wordType, wordList, wordTag

	def compareLists(self, targetList, evaluateList):

		for i in range(len(evaluateList)-len(targetList)+1):
			for j in range(len(targetList)):
				if evaluateList[i+j] != targetList[j]:
					break
			else:
				return True
		return False
