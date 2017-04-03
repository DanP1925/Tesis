class opinionNode:

		def __init__(self, i, sentiment):
			self.index = i
			self.sentiment = sentiment
			self.edges = []
			
		def setEdges(self, sentiments):
			for i in range(0,self.sentiments):
				if self.index != j:
					self.edges.append(self.sentiment.similarity(self.sentiment[i]),lsa)
				
				
		# for i in range(0,len(self.sentiments)):
			# list = []
			# for j in range(0,len(self.sentiments)):
				# if i != j:
					# list.append(self.sentiments[i].similarity(self.sentiments[j],lsa))
				# else:
					# list.append(0)
			# min = self.minimumValue(list, math.ceil(self.numberOfReviews/5))
			# for element in list:
				# if element < min
					# element = 0
			# self.sentiments[i].calculateDegree(list)
			# self.matrix.append(list)