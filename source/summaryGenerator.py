import math
import random

class summaryGenerator:
	
	def __init__(self):
		self.summary = ''


	def firstSentence(self, entityName, aspectName):
		random.seed()

		name = self.removeUnderLine(entityName)
		self.summary += 'De la entidad ' + name + ' se tiene como caracteristica principal al ' + self.removeUnderLine(aspectName) + '. '

	def aspectMain(self, aspectName, mainType, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText):
		random.seed()
	
		if bimodal :
			yEllos = False
			if relFreq > 0.6:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'La mayoría de usuarios que comentaron del aspecto '
				elif num == 1:
					self.summary += 'La mayoría de personas mencionaron al aspecto '
					yEllos = True
			elif relFreq > 0.45:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'Casi la mitad de los usuarios que comentaron del aspecto '
				elif num == 1:
					self.summary += 'Casi el 50% de las personas mencionaron al aspecto '
					yEllos = True

			self.summary += self.removeUnderLine(aspectName)
			if yEllos:
				self.summary += 'y ellos '

			num = random.randint(0,1)
			if num == 0:
				self.summary += ' tenían opiniones controversiales sobre él. '
			elif num == 1:
				self.summary += ' expresabas opioniones controversiales sobre esa característica. '

			num = random.randint(0,1)
			if num == 0:
				self.summary += 'Por un lado, '
			elif num == 1:
				self.summary += 'Por una parte, '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'algunos estaban a favor debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					self.summary += 'algunos pensaban que era bueno debido a ' + self.restore(mainFull, alternateText) + '. '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					self.summary += 'algunos pensaban que era malo debido a ' + self.restore(mainFull, alternateText) + '. '
		else:
			if relFreq == 1:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'Todos los usuarios que comentaron del aspecto ' 
				elif num == 1:
					self.summary += 'Todas las personas que se expresaron del aspecto '
			elif relFreq > 0.8:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'Casi todos los usuarios que comentaron del aspecto '
				elif num == 1:
					self.summary += 'Casi todas las personas que mencionaron el aspecto '
			elif relFreq > 0.7:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'La mayoría de usuarios que comentaron del aspecto '
				elif num == 1:
					self.summary += 'La mayoría de personas que mencionaron el aspecto '

			self.summary += self.removeUnderLine(aspectName) + ' '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'les gusto debido a '
				elif num == 1:
					self.summary += 'les agrado debido a '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'les disgusto debido a '
				elif num == 1:
					self.summary += 'les desagrado debido a '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '. '
			else:
				self.summary += alternateText + '.'

	def aspectOpposite(self, lastPolarity, mainType, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText):
		random.seed()

		if bimodal:
			num = random.randint(0,1)
			if num == 0:
				self.summary += 'Por otro lado, '
			elif num == 1:
				self.summary += 'Por otra parte, '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'algunos estaban a favor debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					self.summary += 'algunos pensaban que era bueno debido a ' + self.restore(mainFull, alternateText) + '. '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					self.summary += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
		else:
			num = random.randint(0,1)
			if num == 0:
				self.summary += 'Sin embargo, '
			elif num == 1:
				self.summary += 'En cambio, '

			if relFreq > 0.6:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'la mayoría de usuarios comentaron del aspecto '
				elif num == 1:
					self.summary += 'la mayoría de personas mencionaron del aspecto '
			elif relFreq > 0.45:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'casi la mitad de de usuarios mencionaron del aspecto '
				elif num == 1:
					self.summary += 'casi el 50% de las personas mencionaron del aspecto ' 
			elif relFreq > 0.2:
				num = random.randint(0,1)
				if num == 0:
					self.summary += 'cerca del ' + str(math.ceil(relFreq * 100)) + ' % comentaron del aspecto '
				elif num == 1:
					self.summary += 'ceraca del' + str(math.ceil(relFreq * 100)) + ' % mencionaron del aspecto '
			elif relFreq >= 0:
				if absFreq >= 2:
					self.summary += 'algunos usuarios comentaron del aspecto '
				elif absFreq == 1:
					self.summary += 'un usuario comentó del aspecto '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					self.summary += ' que les gusto debido a '
				elif num == 1:
					self.summary += ' que les agrado debido a '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					self.summary += ' que les disgusto debido a '
				elif num == 1:
					self.summary += ' que les desagrado debido a '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '. '
			else:
				self.summary += alternateText + '. '

	def aspectSupport(self, lastPolarity, mainType, mainFull, polarity, relFreq, absFreq, alternateText):
		random.seed()

		if lastPolarity == polarity:
			num = random.randint(0,1)
			if num == 0:
				self.summary += 'De la misma manera, a los usuarios también '
			elif num == 1:
				self.summary += 'Del mismo modo, a los usuarios también '
		else:
			num = random.randint(0,1)
			if num == 0:
				self.summary += 'Pero en lo que respecta al aspecto, a los usuarios '
			elif num == 1:
				self.summary += 'Pero en lo que respecta al aspecto, a las personas '
		
		if polarity == 'P':
			num = random.randint(0,1)
			if num == 0:
				self.summary += ' les gusto debido al '
			elif num == 1:
				self.summary += ' les agrado debido al '
		elif polarity == 'N':
			num = random.randint(0,1)
			if num == 0:
				self.summary += ' les disgusto debido al '
			elif num == 1:
				self.summary += ' les desagrado debido al '

		if mainType is not None:
			if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
				self.summary += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
			
			if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
				self.summary += 'acto de ' + self.restore(mainFull, alternateText) + '. '
		else:
			self.summary += alternateText + '. '

	def removeUnderLine(self, name):
		random.seed()

		newName = ''
		wordList = name.split('_')
		for element in wordList:
			newName += element + ' '
		return newName
		

	def restore(self, mainList, alternateText):
		random.seed()

		result = ''
		if mainList is None:
			return alternateText
		for element in mainList:
			if element == '@':
				result += element
			else:
				result += element + ' '
		return result
