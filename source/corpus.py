import entity as ENT

class Corpus:
	
	def __init__(self):
		self.entities = []
	
	def isInEntities(self, value):
		for entity in self.entities:
			if entity.name == value:
				return True
		return False
	
	def addNewEntities(self, newEntities):
		for newEntity in newEntities:
			if not self.isInEntities(newEntity):
				self.entities.append(ENT.Entity(newEntity))
				
	def asEntityList(self):
		result = []
		for entity in self.entities:
			result.append(entity.name)
		return result
		
	def getEntity(self, value):
		for entity in self.entities:
			if entity.name == value:
				return entity
		return None
	
	def debug(self):
		for entity in self.entities:
			entity.debug()
			print()