
class Community:
	
	def __init__(self,leader):
		self.leader = leader
		self.elements = []
		self.elements.append(leader)
		
	def updateScore(self, nodes, reviews):
		for element in self.elements:
			importanceOfReview = self.getReviewScore(nodes[element].sentiment.text, reviews)
			importanceOfSentiment = self.centrality(nodes[element].edges)
			nodes[element].score = importanceOfReview * importanceOfSentiment
			
	def getReviewScore(self, text, reviews):
		maxvalue = -1
		for review in reviews:
			for sentiment in review.sentiments:
				if sentiment.text == text:
					if maxvalue < review.score:
						maxvalue = review.score
		return maxvalue
		
	def centrality(self, edges):
		neighbors = 0
		for i in range(0,len(edges)):
			if edges[i] > 0 and i in self.elements:
				neighbors +=1
		if (len(self.elements)<2):
			return 0
		return neighbors/(len(self.elements)-1)
		
	def updateLeader(self, nodes):
		maxvalue = -1
		for i in range(0,len(nodes)):
			if nodes[i].score > maxvalue and i in self.elements:
				maxvalue = nodes[i].score
				self.leader = i
		
	def debug(self, nodes):
		print('Leader: ',end =' ')
		print(nodes[self.leader].sentiment.text)	
		for element in self.elements:
			print(nodes[element].sentiment.text)
		print()
		
	