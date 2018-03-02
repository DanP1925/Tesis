import sentiment as SEN

class review:
	
    def __init__(self, tweet):
        self.text = self.rawText(tweet)
        self.sentiments = self.setSentiments(tweet)
        self.score = 0
		
    def rawText(self,tweet):
        if tweet.text is not None:
            full = tweet.text
        else:
            full = ""
        for sentiment in tweet:
            if sentiment.text is not None:
                full+=sentiment.text
            if sentiment.tail is not None:
                full +=sentiment.tail
        return full
		
    def setSentiments(self, tweet):
        sentiments = []
        for sentiment in tweet:
            sentiments.append(SEN.Sentiment(sentiment.text, sentiment.get('aspect'), sentiment.get('polarity')))
        return sentiments
		
    def updateScore(self, nodes):
        sum = 0
        for sentiment in self.sentiments:
            for node in nodes:
                if sentiment.text == node.sentiment.text:
                    sum += node.score
                    break
        self.score = sum/len(self.sentiments)
					
			
    def debug(self):
        print("Text")
        print(self.text)
        for sentiment in sentiments:
            sentiment.debug()
		
