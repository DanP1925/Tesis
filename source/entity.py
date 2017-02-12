class Entity:

	def __init__(self, name):
		self.name = name
		self.aspects = []
		self.opinions = []
		
	def addNewAspects(self, newAspects):
		for newAspect in newAspects:
			if not newAspect in self.aspects:
				self.aspects.append(newAspect)
			
			
	