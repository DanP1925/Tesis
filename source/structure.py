import structureItem as strItem
import math

class Structure:
    
    def __init__(self):
        self.summaryOrder = []
		
    def assignOrder(self, communities, graph):
        self.getAspects(graph.nodes)
        self.getRepresentatives(communities, graph)
        self.getFrequencies(graph.nodes)
        self.orderList(graph.nodes)		
        self.getSupportiveSentences(graph.nodes)

    def getAspects(self, nodes):
        aspectList = []
        for node in nodes:
            aspect = node.sentiment.aspect
            if aspect not in aspectList:
                aspectList.append(aspect)
                self.summaryOrder.append(strItem.structureItem(aspect))
		
    def getRepresentatives(self, communities, graph):
        for element in self.summaryOrder:
            element.getLeaderRepresentative(communities, graph)	
            if element.representative is None:
                element.getRepresentative(graph.nodes)

    def getFrequencies(self, nodes):
        for element in self.summaryOrder:
            element.getFrequencies(nodes)
		
    def orderList(self, nodes):
        n = len(self.summaryOrder)	
        while True:
            swapped = False
            for i in range(1,n):
                if self.importance(self.summaryOrder[i-1], nodes) < self.importance(self.summaryOrder[i], nodes):
                    self.summaryOrder[i -1] , self.summaryOrder[i] = self.summaryOrder[i] , self.summaryOrder[i-1]
                    swapped = True		
            if not swapped:
                break
					 
    def importance(self, structureItem, nodes):
        if structureItem.representative is None:
            return 0

        relevanceFactor = 0.7
        positiveFactor = 1.0 / 3
        negativeFactor = 1.0 / 3
        controversyFactor = 1.0 / 3

        relevance = nodes[structureItem.representative].score	
        positiveValue = positiveFactor * structureItem.relPositiveFreq
        negativeValue = negativeFactor * structureItem.relNegativeFreq
        controverseValue = controversyFactor * min(structureItem.relPositiveFreq , structureItem.relNegativeFreq)/max(structureItem.relPositiveFreq , structureItem.relNegativeFreq)

        controversy = positiveValue + negativeValue  + controverseValue 
        return (relevance * relevanceFactor) + (controversy * (1 - relevanceFactor))

    def getSupportiveSentences(self, nodes):
        for element in self.summaryOrder:
            if element.representative is not None:
                element.getOppositeOpinion(nodes)
                if element.relPositiveFreq > 0.7 or element.relNegativeFreq > 0.7:
                    element.getSupportiveOpinion(nodes)					

    def printOrder(self, nodes):
        for element in self.summaryOrder:
            element.printItem(nodes)
