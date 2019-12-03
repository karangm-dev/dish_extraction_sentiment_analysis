import re
import numpy as np

class Preprocessing:

    @staticmethod
    def preprocess_review_text(review):
        # Remove spaces at each end
        review = review.strip()

        review = review.replace("\\n", ".")

        # Remove backslash
        review = review.replace("\\", "")

        # Remove duplicate spaces
        review = re.sub(' +', ' ', review)

        # Replace .., !!!!,....etc
        review = re.sub(r'(\W)\1+', r'\1', review)

        return review

    @staticmethod
    def preprocess_golden_truth_text(golden_truth_text):
        # If there is no gold truth available - no dishes in the review
        if golden_truth_text is np.nan:
            return None

        dish_sentiment_dict = {}
        golden_truth_text_lines = golden_truth_text.split("\n")
        for dish_sentiment in golden_truth_text_lines:
            dish_sentiment = dish_sentiment.split(',')
            dish = dish_sentiment[0].strip()
            dish=dish.strip('\"')
            sentiment = None
            if len(dish_sentiment) == 1:
                # This is a candidate for sentiment being neutral
                sentiment = 0
            else:
                temp_sentiment = dish_sentiment[1].strip()
                if temp_sentiment == '+':
                    sentiment = 1
                elif temp_sentiment == '-':
                    sentiment = -1
            dish_sentiment_dict[dish] = {'sentiment': sentiment}
        return dish_sentiment_dict