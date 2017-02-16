import opinion as OP

class Entity:

	def __init__(self, name):
		self.name = name
		self.aspects = []
		self.opinions = []
		
	def isInOpinions(self,value):
		for opinion in self.opinions:
			if opinion.opinion == value:
				return True
		return False
		
	def addNewAspects(self, newAspects):
		for newAspect in newAspects:
			if not newAspect in self.aspects:
				self.aspects.append(newAspect)
	
	def addNewOpinion(self, newOpinion):
		for opinion in self.opinions:
			if self.isInOpinions(newOpinion):
				return
		self.opinions.append(OP.Opinion(newOpinion))
	
	def debug(self):
		print('Entity: ')
		print('Name: ' + self.name)
		for aspect in self.aspects:
			print('Aspect: ')
			print(aspect)
		for opinion in self.opinions:
			opinion.debug()