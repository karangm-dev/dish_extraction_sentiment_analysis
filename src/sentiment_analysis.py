from textblob import TextBlob
import paralleldots
from config import Config

class SentimentAnalysis:
        @staticmethod
        def run(text,lib='textblob'):
            try:
                if lib =='paralleldot':
                    # Setting your API key
                    paralleldots.set_api_key(Config.PARALLEL_DOT_API_KEY)

                    # Viewing your API key
                    paralleldots.get_api_key()
                    sentiment = paralleldots.sentiment(text)['sentiment']
                    return max(sentiment, key=sentiment.get)
                else:
                    testimonial = TextBlob(text)
                    return testimonial.sentiment.polarity

            except Exception as e:
                print(e)
                return 'neutral'







