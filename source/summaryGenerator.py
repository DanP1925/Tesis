import math
import random

class summaryGenerator:
	
	def __init__(self, size):
		self.summary = [None] * (size + 1)

	def firstSentence(self, entityName, aspectName):
		random.seed()

		name = self.removeUnderLine(entityName)
		self.summary[0] = 'De la entidad ' + name + ' se tiene como caracteristica principal al ' + self.removeUnderLine(aspectName) + '. '

	def aspectMain(self, aspectName, mainType, mainTag, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText, i):
		random.seed()

		sentence = ''
		if bimodal :
			yEllos = False
			if relFreq > 0.6:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'La mayoría de usuarios que comentaron del aspecto '
				elif num == 1:
					sentence += 'La mayoría de personas mencionaron al aspecto '
					yEllos = True
			elif relFreq > 0.45:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'Casi la mitad de los usuarios que comentaron del aspecto '
				elif num == 1:
					sentence += 'Casi el 50% de las personas mencionaron al aspecto '
					yEllos = True

			sentence += self.removeUnderLine(aspectName)
			if yEllos:
				sentence += 'y ellos '

			num = random.randint(0,1)
			if num == 0:
				sentence += ' tenían opiniones controversiales sobre él. '
			elif num == 1:
				sentence += ' expresabas opioniones controversiales sobre esa característica. '

			num = random.randint(0,1)
			if num == 0:
				sentence += 'Por un lado, '
			elif num == 1:
				sentence += 'Por una parte, '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'algunos estaban a favor debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					sentence += 'algunos pensaban que era bueno debido a ' + self.restore(mainFull, alternateText) + '. '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					sentence += 'algunos pensaban que era malo debido a ' + self.restore(mainFull, alternateText) + '. '
		else:
			if relFreq == 1:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'Todos los usuarios que comentaron del aspecto ' 
				elif num == 1:
					sentence += 'Todas las personas que se expresaron del aspecto '
			elif relFreq > 0.8:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'Casi todos los usuarios que comentaron del aspecto '
				elif num == 1:
					sentence += 'Casi todas las personas que mencionaron el aspecto '
			elif relFreq > 0.7:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'La mayoría de usuarios que comentaron del aspecto '
				elif num == 1:
					sentence += 'La mayoría de personas que mencionaron el aspecto '

			sentence += self.removeUnderLine(aspectName) + ' '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'les gusto debido a '
				elif num == 1:
					sentence += 'les agrado debido a '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'les disgusto debido a '
				elif num == 1:
					sentence += 'les desagrado debido a '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					sentence += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					sentence += 'acto de ' + self.restore(mainFull, alternateText) + '. '
			else:
				sentence += alternateText + '.'
		self.summary[i+1] = [sentence,None,None]


	def aspectOpposite(self, lastPolarity, mainType, mainTag, mainFull, polarity,  bimodal, relFreq, absFreq, alternateText, i):
		random.seed()

		sentence = ''
		if bimodal:
			num = random.randint(0,1)
			if num == 0:
				sentence += 'Por otro lado, '
			elif num == 1:
				sentence += 'Por otra parte, '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'algunos estaban a favor debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					sentence += 'algunos pensaban que era bueno debido a ' + self.restore(mainFull, alternateText) + '. '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					sentence += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
				elif num == 1:
					sentence += 'algunos estaban en contra debido a ' + self.restore(mainFull, alternateText) + '. '
		else:
			num = random.randint(0,1)
			if num == 0:
				sentence += 'Sin embargo, '
			elif num == 1:
				sentence += 'En cambio, '

			if relFreq > 0.6:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'la mayoría de usuarios comentaron del aspecto '
				elif num == 1:
					sentence += 'la mayoría de personas mencionaron del aspecto '
			elif relFreq > 0.45:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'casi la mitad de de usuarios mencionaron del aspecto '
				elif num == 1:
					sentence += 'casi el 50% de las personas mencionaron del aspecto ' 
			elif relFreq > 0.2:
				num = random.randint(0,1)
				if num == 0:
					sentence += 'cerca del ' + str(math.ceil(relFreq * 100)) + ' % comentaron del aspecto '
				elif num == 1:
					sentence += 'ceraca del' + str(math.ceil(relFreq * 100)) + ' % mencionaron del aspecto '
			elif relFreq >= 0:
				if absFreq >= 2:
					sentence += 'algunos usuarios comentaron del aspecto '
				elif absFreq == 1:
					sentence += 'un usuario comentó del aspecto '

			if polarity == 'P':
				num = random.randint(0,1)
				if num == 0:
					sentence += ' que les gusto debido a '
				elif num == 1:
					sentence += ' que les agrado debido a '
			elif polarity == 'N':
				num = random.randint(0,1)
				if num == 0:
					sentence += ' que les disgusto debido a '
				elif num == 1:
					sentence += ' que les desagrado debido a '

			if mainType is not None:
				if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
					sentence += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
				
				if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
					sentence += 'acto de ' + self.restore(mainFull, alternateText) + '. '
			else:
				sentence += alternateText + '. '

		self.summary[i+1][1]=sentence

	def aspectSupport(self, lastPolarity, mainType, mainTag, mainFull, polarity, relFreq, absFreq, alternateText, i):
		random.seed()

		sentence = ''
		if lastPolarity == polarity:
			num = random.randint(0,1)
			if num == 0:
				sentence += 'De la misma manera, a los usuarios también '
			elif num == 1:
				sentence += 'Del mismo modo, a los usuarios también '
		else:
			num = random.randint(0,1)
			if num == 0:
				sentence += 'Pero en lo que respecta al aspecto, a los usuarios '
			elif num == 1:
				sentence += 'Pero en lo que respecta al aspecto, a las personas '
		
		if polarity == 'P':
			num = random.randint(0,1)
			if num == 0:
				sentence += ' les gusto debido al '
			elif num == 1:
				sentence += ' les agrado debido al '
		elif polarity == 'N':
			num = random.randint(0,1)
			if num == 0:
				sentence += ' les disgusto debido al '
			elif num == 1:
				sentence += ' les desagrado debido al '

		if mainType is not None:
			if mainType == 'sn' or mainType == 'grup-sp-inf' or mainType == 'grup-sp':
				sentence += 'hecho de ' + self.restore(mainFull, alternateText) + '. '
			
			if mainType == 'grup-verb' or mainType == 'grup-verb-inf': 
				sentence += 'acto de ' + self.restore(mainFull, alternateText) + '. '
		else:
			sentence += alternateText + '. '

		self.summary[i+1][2]=sentence

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
