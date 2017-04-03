import sentiment as SEN

class review:
	
	def __init__(self, tweet):
		self.text = self.rawText(tweet)
		self.sentiments = self.setSentiments(tweet)
		
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
			
	def debug(self):
		print("Text")
		print(self.text)
		for sentiment in sentiments:
			sentiment.debug()
		