class Entities:
	entities = dict()
	
	def addNewEntities(self, newEntities):
		for entity in newEntities:
			if entity not in self.entities:
				self.entities[entity] = None
	
	def printEntities(self):
		for key in self.entities:
			print(key)