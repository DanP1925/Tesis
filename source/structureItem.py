class structureItem:
	
    def __init__(self, aspect):
        self.aspect = aspect
        self.representative = None 
        self.representativeType = None
        self.representativeFull = None
        self.opposite = None
        self.oppositeType = None
        self.oppositeFull = None
        self.support = None
        self.supportType = None
        self.supportFull = None
        self.relPositiveFreq = 0
        self.relNegativeFreq = 0
        self.absPositiveFreq = 0
        self.absNegativeFreq = 0

    def getLeaderRepresentative(self, communities, graph):
        max = -1
        representative = -1
        for community in communities:
            aspect = graph.nodes[community.leader].sentiment.aspect
            polarity = graph.nodes[community.leader].sentiment.polarity
            if aspect == self.aspect and polarity != 'NEU':
                if graph.nodes[community.leader].score > max:
                    max = graph.nodes[community.leader].score 
                    representative = community.leader
        if representative != -1:
            self.representative =  representative

    def getRepresentative(self, nodes):
        max = -1
        representative = -1
        for i in range(0,len(nodes)):
            aspect = nodes[i].sentiment.aspect
            polarity = nodes[i].sentiment.polarity
            if aspect == self.aspect and polarity != 'NEU':
                score = nodes[i].score
                if score > max:
                    max = score
                    representative = i
        if representative != -1:
            self.representative = representative

    def getFrequencies(self, nodes):
        positive = 0
        negative = 0
        total = 0
        for node in nodes:
            if node.sentiment.aspect == self.aspect:
                if node.sentiment.polarity == 'P':
                    positive += 1
                elif node.sentiment.polarity == 'N':
                    negative += 1
                total +=1
        self.absPositiveFreq = positive
        self.absNegativeFreq = negative 
        self.relPositiveFreq = positive/total
        self.relNegativeFreq = negative/total

    def getOppositeOpinion(self, nodes):
        max = -1
        opposite = -1
        for i in range(0, len(nodes)):
            aspect = nodes[i].sentiment.aspect
            if aspect == self.aspect:
                selfPolarity = nodes[self.representative].sentiment.polarity 
                targetPolarity = nodes[i].sentiment.polarity	
                if self.isOppositePolarity(selfPolarity, targetPolarity):
                    score = nodes[i].score
                    if score > max:
                        max = score
                        opposite = i
        if opposite != -1:
            self.opposite = opposite

    def isOppositePolarity(self, selfPolarity, targetPolarity):
        if selfPolarity == 'P':
            if targetPolarity == 'N':
                return True
        elif selfPolarity == 'N':
            if targetPolarity == 'P':
                return True 
        return False

    def getSupportiveOpinion(self, nodes):
        max = -1
        support = -1
        for i in range(0, len(nodes)):
            aspect = nodes[i].sentiment.aspect
            if aspect == self.aspect:
                selfPolarity = nodes[self.representative].sentiment.polarity
                targetPolarity = nodes[i].sentiment.polarity
                if selfPolarity == targetPolarity and self.representative != i:
                    score = nodes[i].score
                    if score > max:
                        max = score
                        support = i
        if support != -1:
            self.support = support

    def parseRepresentatives(self, freelingAux, nodes, reviews):
        if self.representative is not None:
            rawText = self.getRawText(nodes[self.representative].sentiment, reviews)
            if rawText[-1] != '.' and rawText[-1] != '?':
                rawText += '.'
            sentimentText = nodes[self.representative].sentiment.text
            self.representativeType, self.representativeFull = freelingAux.fullParsing(rawText, sentimentText)

        if self.opposite is not None:
            rawText = self.getRawText(nodes[self.opposite].sentiment, reviews)
            if rawText[-1] != '.' and rawText[-1] != '?':
                rawText += '.'
            sentimentText = nodes[self.opposite].sentiment.text
            self.oppositeType, self.oppositeFull = freelingAux.fullParsing(rawText, sentimentText)

        if self.support is not None:
            rawText = self.getRawText(nodes[self.support].sentiment, reviews)
            if rawText[-1] != '.' and rawText[-1] != '?':
                rawText += '.'
            sentimentText = nodes[self.support].sentiment.text
            self.supportType, self.supportFull = freelingAux.fullParsing(rawText, sentimentText)

    def getRawText(self, targetSentiment, reviews):
        for review in reviews:
            for sentiment in review.sentiments:
                if sentiment == targetSentiment:
                    return review.text
	
    def printItem(self, nodes):
        print(self.aspect)
        if self.representative is not None:
            print(str(self.representative) + ': ' + nodes[self.representative].sentiment.text)
            if self.opposite is not None:
                print('Opposite ' +  str(self.opposite) + ': ' + nodes[self.opposite].sentiment.text)
            if self.support is not None:
                print('Support ' + str(self.support) + ': ' + nodes[self.support].sentiment.text)
            print('Relative frequencies: ' + str(self.relPositiveFreq)  + ' ' + str(self.relNegativeFreq))
            print('Absolute frequencies: ' + str(self.absPositiveFreq)  + ' ' + str(self.absNegativeFreq))
            print('-----------------------------')

