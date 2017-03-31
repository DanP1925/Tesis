import opinionNode as NOD
class opinionGraph:
		
	def __init__(self):
			self.nodes = []
			
	def setNodes(self, sentiments):
		for i in range(0,len(sentiments)):
			newNode = NOD.opinionNode(i, sentiments[i])
			self.nodes.append(newNode)
		
	def setEdges(self, sentiments):
		for node in self.nodes:
			node.setEdges(sentiments)