from preprocessing import Preprocessing
import pandas as pd
from grammar_score import GrammarScore
from coreference_resolution import CoreferenceResolution
from sentiment_analysis import SentimentAnalysis
from sentence_tokenization import SentenceTokenization
from factory import Factory
import pickle

import pprint
pp = pprint.PrettyPrinter(width=200, compact=True)

class DishSentimentAnalysisApp:

    @staticmethod
    def run(input_filepath):
        result_dict = {}
        print("Processing: {}".format(input_filepath))
        file_df = pd.read_csv(input_filepath)

        # Read one review
        for index, row in file_df.iterrows():

            temp_review_dict = {}

            review_id = row['review_id']
            review = row['text']
            golden_truth_text = row['Dishnames, Sentiment']

            golden_truth_dish_sentiment_dict = Preprocessing.preprocess_golden_truth_text(golden_truth_text)
            if golden_truth_dish_sentiment_dict is None:
                continue
            print(review_id)
            review = Preprocessing.preprocess_review_text(review)

            # Check the grammaticality scores
            readability_dict = GrammarScore.get_scores(review)

            # Coreference resolution of the original text
            resolved_review = CoreferenceResolution.run(review)

            # Divide text into sentences
            sentence_tokens = SentenceTokenization.get_sentence_tokens(resolved_review, 'spacy')

            # Create dish buckets and assign valid sentences to dish
            predicted_truth_dish_sentiment_dict = {}
            for dish_names in golden_truth_dish_sentiment_dict:
                predicted_truth_dish_sentiment_dict[dish_names] = {'found':False, 'sentiment': -100, 'sentences':[]}
            # Add a key to handle sentences which do not match to any dish name
            predicted_truth_dish_sentiment_dict['UNK'] = {'sentiment': -100, 'sentences':[]}

            # Feed line by line to the client to detect dish names
            sentence_analysis_list = []
            for sentence in sentence_tokens:
                intent, dish_names = Factory.sclient.detect_intent_for_text(sentence)
                sentence_analysis_list.append((sentence, intent, dish_names))
                if intent == 'Default Fallback Intent':
                    predicted_truth_dish_sentiment_dict['UNK']['sentences'].append(sentence)
                elif (intent == 'menu_item_identification_intent') & (len(dish_names) == 0):
                    predicted_truth_dish_sentiment_dict['UNK']['sentences'].append(sentence)
                else:
                    for dish in dish_names:
                        if dish in predicted_truth_dish_sentiment_dict:
                            predicted_truth_dish_sentiment_dict[dish]['found'] = True
                            predicted_truth_dish_sentiment_dict[dish]['sentences'].append(sentence)

            # Get the sentiment of each dish
            for dish in predicted_truth_dish_sentiment_dict.keys():
                if dish == 'UNK':
                    continue
                else:
                    if dish not in predicted_truth_dish_sentiment_dict:
                        continue
                    else:
                        # Dish name was found and atleast one sentence exists
                        if predicted_truth_dish_sentiment_dict[dish]['found'] == True:
                            # Join all the sentences and get the sentiment
                            sentiment_text = ""
                            for sentence in predicted_truth_dish_sentiment_dict[dish]['sentences']:
                                sentiment_text = sentiment_text + sentence
                            predicted_truth_dish_sentiment_dict[dish]['sentiment'] = SentimentAnalysis.run(sentiment_text)

            temp_review_dict = {
                'text': review,
                'readability_scores': readability_dict,
                'golden_truth': golden_truth_dish_sentiment_dict,
                'predicted_truth': predicted_truth_dish_sentiment_dict,
                'sentences': sentence_analysis_list
            }

            # pp.pprint(temp_review_dict)

            # Save it in the dictionary
            result_dict[review_id] = temp_review_dict

        # Save the overall dictionary
        output_filepath = '../output/' + input_filepath[input_filepath.rfind('/')+1:input_filepath.rfind('.csv')] + '.p'
        with open(output_filepath, 'wb') as pickle_dump_file_pointer:
            pickle.dump(result_dict, pickle_dump_file_pointer, protocol=pickle.HIGHEST_PROTOCOL)

DishSentimentAnalysisApp.run('../input/test/test_sample.csv')
