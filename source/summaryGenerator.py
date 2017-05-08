import math

class summaryGenerator:
	
	def __init__(self):
		self.summary = ''


	def firstSentence(self, entityName, aspectName):
		name = self.removeUnderLine(entityName)
		self.summary += 'De la entidad ' + name + ' se tiene como caracteristica principal al ' + self.removeUnderLine(aspectName) + '. '

	def aspectMain(self, aspectName, mainType, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText):
		if bimodal :
			if relFreq > 0.6:
				self.summary += 'La mayoría de usuarios que comentaron del aspecto '
			elif relFreq > 0.45:
				self.summary += 'Casi la mitad de los usuarios que comentaron del aspecto '

			self.summary += self.removeUnderLine(aspectName) + ' tenían opiniones controversiales sobre él. '

			if polarity == 'P':
				self.summary += 'Por un lado, algunos estaba a favor debido a ' + self.restore(mainFull, alternateText) + '.'
			elif polarity == 'N':
				self.summary += 'Por un lado, algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '.'
		else:
			if relFreq == 1:
				self.summary += 'Todos los usuarios que comentaron del aspecto ' 
			elif relFreq > 0.8:
				self.summary += 'Casi todos los usuarios que comentaron del aspecto '
			elif relFreq > 0.7:
				self.summary += 'La mayoría de usuarios que comentaron del aspecto '

			self.summary += self.removeUnderLine(aspectName) + ' '

			if polarity == 'P':
				self.summary += 'les gusto debido al '
			elif polarity == 'N':
				self.summary += 'les disgusto debido al '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '.'
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '.'
			else:
				self.summary += alternateText + '.'

	def aspectOpposite(self, lastPolarity, mainType, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText):
		if bimodal:
			if polarity == 'P':
				self.summary += 'Por otro lado, algunos estaban a favor debido a ' + self.restore(mainFull, alternateText) + '.'
			elif polarity == 'N':
				self.summary += 'Por otro lado, algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '.'
		else:
			if relFreq > 0.6:
				self.summary += 'Sin embargo, la mayoría de usuarios comentaron del aspecto '
			elif relFreq > 0.45:
				self.summary += 'Sin embargo, casi la mitad de de usuarios mencionaron del aspecto '
			elif relFreq > 0.2:
				self.summary += 'Sin embargo, cerca del ' + str(math.ceil(relFreq * 100)) + ' % comentaron del aspecto '
			elif relFreq >= 0:
				if absFreq >= 2:
					self.summary += 'Sin embargo, algunos usuarios comentaron del aspecto '
				elif absFreq == 1:
					self.summary += 'Pese a eso, un usuario comentó del aspecto '
			
			if polarity == 'P':
				self.summary += 'que les gusto debido al '
			elif polarity == 'N':
				self.summary += 'que les disgusto debido al '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '.'
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '.'
			else:
				self.summary += alternateText + '.'

	def aspectSupport(self, lastPolarity, mainType, mainFull, polarity, relFreq, absFreq, alternateText):
		if lastPolarity == polarity:
			self.summary += 'De la misma manera, a los usuarios también '
		else:
			self.summary += 'Pero en lo que respecta al aspecto, a los usuarios '
		
		if polarity == 'P':
			self.summary += ' les gusto debido al '
		elif polarity == 'N':
			self.summary += ' les disgusto debido al '

		if mainType is not None:
			if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
				self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '.'
			
			if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
				self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '.'
		else:
			self.summary += alternateText + '.'

	def removeUnderLine(self, name):
		newName = ''
		wordList = name.split('_')
		for element in wordList:
			newName += element + ' '
		return newName
		

	def restore(self, mainList, alternateText):
		result = ''
		if mainList is None:
			return alternateText
		for element in mainList:
			if element == '@':
				result += element
			else:
				result += element + ' '
		return result
