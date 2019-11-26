from textblob import TextBlob

class SentimentAnalysis:

    @staticmethod
    def run(text):
        testimonial = TextBlob(text)
        return testimonial.sentiment.polarity
