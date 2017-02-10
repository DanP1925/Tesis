class Corpus:
	entities = []	
	
	def addNewEntities(self, newEntities):
		for entity in newEntities:
			if entity not in self.entities:
				self.entities[entity] = [[],[]]
	
	def addNewAspect(self, entity, newAspect):
		if newAspect not in entities[entity][0]:
			return
	
	def debug(self):
		for key in self.entities:
			print(key)