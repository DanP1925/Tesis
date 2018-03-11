import review as REV
import opinionGraph as GRAPH
import operator
import community as COMM
import math
import structure as STRUCT
import freelingLibrary as FL
import summaryGenerator as SG

class Entity:

    def __init__(self, name, positiveFactor, negativeFactor, controversyFactor):
        self.name = name
        self.reviews = []
        self.graph = GRAPH.opinionGraph()
        self.matrix = []
        self.leaders = []
        self.communities = []
        self.outliers = []
        self.structure = STRUCT.Structure(positiveFactor, negativeFactor, controversyFactor)

    def addReview(self,tweet):
        newReview = REV.review(tweet)
        self.reviews.append(newReview)
			
    def obtainLeaders(self):
        self.graph.setNeighborNumber(self.reviews)
        self.graph.setNodes(self.reviews)
        self.graph.setEdges()

        self.initializeLeaders()

    def initializeLeaders(self):
        hnodes = self.graph.obtainHNodes()
        hnodes.sort(reverse=True)
        while len(hnodes) != 0:
            hnode = hnodes.pop(0)
            if not self.graph.hasLeaderNeighbors(hnode[1], self.leaders):
                self.leaders.append(hnode[1])
	
    def obtainCommunities(self):
        self.initializeReviewScore()
        prevLeaders = list(self.leaders)
        while True:
            del self.communities[:]
            del self.outliers[:]
            self.initializeCommunities()
            self.graph.setDistances(self.leaders)
            distances = self.graph.getDistances()
            distances = self.sortDistances(distances)
            for element in distances:
                self.assignCommunity(element[0])
            for i in range(0,len(self.communities)):
                self.communities[i].updateScore(self.graph.nodes, self.reviews)
                self.communities[i].updateLeader(self.graph.nodes)
                self.leaders[i] = self.communities[i].leader
            for review in self.reviews:
                review.updateScore(self.graph.nodes)
            if prevLeaders == self.leaders:
                break
            prevLeaders = list(self.leaders)
		
    def initializeCommunities(self):
        for leader in self.leaders:
            self.communities.append(COMM.Community(leader))
		
    def initializeReviewScore(self):
        for review in self.reviews:
            review.score = 1/len(self.reviews)
	
    def sortDistances(self, distances):
        n = len(distances)
        sorted = list(distances)
        while True:
            swapped = False
            for i in range(1,n):
                if self.compareDistances(sorted[i-1][1],sorted[i][1]):
                    sorted[i-1],sorted[i] = sorted[i],sorted[i-1]
                    swapped = True
            if swapped == False:
                break
        return sorted
	
    def compareDistances(self, e1, e2):
        infNum1 = 0
        for element in e1:
            if element == float('Inf'):
                infNum1 += 1
        infNum2 = 0
        for element in e2:
            if element == float('Inf'):
                infNum2 += 1
        if infNum2 > infNum1:
            return False
        elif infNum2 < infNum1:
            return True
        else:
            dist1 = 0
            for element in e1:
                if element != float('Inf'):
                    dist1 += pow(element,2)
            dist1 = math.sqrt(dist1)
            
            dist2 = 0
            for element in e2:
                if element != float('Inf'):
                    dist2 += pow(element,2)
            dist2 = math.sqrt(dist2)
            
            if dist1 > dist2:
                return True
            else:
                return False
	
    def assignCommunity(self, index):
        if index not in self.leaders:
            maxcommon = 0
            maxCommunity = -1
            for i in range(0,len(self.communities)):
                num = self.graph.edgesWithCommunity(index,self.communities[i])
                if num > maxcommon:
                    maxcommon = num
                    maxCommunity = i
            if maxCommunity == -1:
                self.outliers.append(index)
            else:
                self.communities[maxCommunity].elements.append(index)
	
    def assignOrder(self):
        self.structure.assignOrder(self.communities,self.graph)

    def fullParsing(self):
        freelingAux = FL.freelingLibrary()
        for structureItem in self.structure.summaryOrder:
            structureItem.parseRepresentatives(freelingAux, self.graph.nodes, self.reviews)
	
    def generateSummary(self):
        max = 120
        summary = SG.summaryGenerator(len(self.structure.summaryOrder))
        
        for i in range(0,len(self.structure.summaryOrder)):
            bimodal = False
            lastPolarity = None
            structureItem = self.structure.summaryOrder[i]
            if i == 0:
                summary.firstSentence(self.name, structureItem.aspect)
            if structureItem.representative is not None:
                reprSentiment = self.graph.nodes[structureItem.representative].sentiment
                if reprSentiment.polarity == 'P':
                    relFreq = structureItem.relPositiveFreq	
                    absFreq = structureItem.absPositiveFreq
                elif reprSentiment.polarity == 'N':
                    relFreq = structureItem.relNegativeFreq
                    absFreq = structureItem.absNegativeFreq
                if relFreq < 0.7:
                    bimodal = True
                summary.aspectMain(structureItem.aspect, structureItem.representativeType, structureItem.representativeTag, structureItem.representativeFull, reprSentiment.polarity, bimodal, relFreq, absFreq, reprSentiment.text, i)
                lastPolarity = reprSentiment.polarity
            if structureItem.opposite is not None:
                oppSentiment = self.graph.nodes[structureItem.opposite].sentiment
                if oppSentiment.polarity == 'P':
                    relFreq = structureItem.relPositiveFreq	
                    absFreq = structureItem.absPositiveFreq
                elif oppSentiment.polarity == 'N':
                    relFreq = structureItem.relNegativeFreq
                    absFreq = structureItem.absNegativeFreq
                summary.aspectOpposite(lastPolarity, structureItem.oppositeType, structureItem.oppositeTag, structureItem.oppositeFull, oppSentiment.polarity, bimodal, relFreq, absFreq, oppSentiment.text, i)
                lastPolarity = oppSentiment.polarity
            if structureItem.support is not None:
                supSentiment = self.graph.nodes[structureItem.support].sentiment
                if supSentiment.polarity == 'P':
                    relFreq = structureItem.relPositiveFreq	
                    absFreq = structureItem.absPositiveFreq
                elif supSentiment.polarity == 'N':
                    relFreq = structureItem.relNegativeFreq
                    absFreq = structureItem.absNegativeFreq
                summary.aspectSupport(lastPolarity, structureItem.supportType, structureItem.supportTag, structureItem.supportFull, supSentiment.polarity, relFreq, absFreq, supSentiment.text, i)

        return summary.summary

    def reestructure(self, summaryList, maxWords):
        result = ''
        flag = False
        flagSummaryList = [None] * len(summaryList)
        for i in range(0,len(flagSummaryList)):
            flagSummaryList[i] = ["","",""]

        if len(summaryList[0]) + len(result) < maxWords:
            result += summaryList[0]
            flagSummaryList[0][0] = summaryList[0]
        else:
            flag = True

        for i in range(1,len(summaryList)):
            if flag:
                break

            element = summaryList[i][0]
            if element is not None:
                if len(element)+len(result) < maxWords:
                    result += element
                    flagSummaryList[i][0] = element
                else:
                    flag = True

        for i in range(1,len(summaryList)):
            if flag:
                break

            element = summaryList[i][1]
            if element is not None:
                if len(element)+len(result) <maxWords:
                    result += element
                    flagSummaryList[i][1] = element
                else:
                    flag = True

        for i in range(1,len(summaryList)):
            if flag:
                break

            element = summaryList[i][2]
            if element is not None:
                if len(element)+len(result) <maxWords:
                    result += element
                    flagSummaryList[i][2] = element
                else:
                    flag = True

        newResult = ''
        for i in range(0,len(summaryList)):
            for j in range(0,3):
                newResult += flagSummaryList[i][j]

        return newResult

    def debug(self):
        print('Entity')
        print(self.name)
        for sentiment in self.sentiments:
            sentiment.debug()
			
    def printCommunities(self):
        for community in self.communities:
            community.debug(self.graph.nodes)
        self.printOutliers(self.graph.nodes)
        print('----------------------------')
		
    def printOutliers(self, nodes):
        print("Outliers:")
        for element in self.outliers:
            print(nodes[element].sentiment.text)
			
