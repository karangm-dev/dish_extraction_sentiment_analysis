import csv
import pickle
import pprint
import numpy as np

pp = pprint.PrettyPrinter(width=200, compact=True)


class Evaluation:

    @staticmethod
    def output_scores(evaluation_dict):
        #Final list
        final_dictionary_list = []
        for key, value in evaluation_dict.items():
            #Creating empty lists for all the columns in the end output csv file
            actual_dishname = []
            actual_sentiment = []
            predicted_dishname = []
            predicted_sentiment = []
            final_predicted_sentiment = []
            ARI_score = []
            Coleman_Liu_score = []
            DaleChallIndex_score = []
            FleschReadingeEase_score = []
            GunningFogIndex_score = []
            Kincaid_score = []
            LIX_score = []
            RIX_score = []
            SMOGIndex_score = []
            dish_extraction_recall = []
            sentiment_extraction_recall = []
            # Extracting ground truth dishnames
            for k in evaluation_dict[key]['golden_truth'].keys():
                actual_dishname.append(k)
            # Extracting ground truth sentiments
            for k in evaluation_dict[key]['golden_truth'].values():
                actual_sentiment.append(k['sentiment'])
            #Extracting predicted truth for dishnames and sentiments
            for i, k in evaluation_dict[key]['predicted_truth'].items():
                #Just look at length 3 for found key
                if len(k) == 3:
                    if k['found']:
                        predicted_dishname.append(i)
                        predicted_sentiment.append(k['sentiment'])
                    else:
                        predicted_sentiment.append(k['sentiment'])
                else:
                    predicted_sentiment.append(k['sentiment'])
            # Rounding up the floating sentiment values , +1 for sentiment >0, -1 for sentiment <0 and nan for sentiment with value -100
            for i in predicted_sentiment:
                if i == -100:
                    final_predicted_sentiment.append(np.nan)
                if i < 0 and i != -100:
                    final_predicted_sentiment.append(-1)
                if i >= 0:
                    final_predicted_sentiment.append(1)
            # Forming seperate lists for all readability scores
            ARI_score.append(evaluation_dict[key]['readability_scores']['ARI'])
            Coleman_Liu_score.append(evaluation_dict[key]['readability_scores']['Coleman-Liau'])
            DaleChallIndex_score.append(evaluation_dict[key]['readability_scores']['DaleChallIndex'])
            FleschReadingeEase_score.append(evaluation_dict[key]['readability_scores']['FleschReadingEase'])
            GunningFogIndex_score.append(evaluation_dict[key]['readability_scores']['GunningFogIndex'])
            Kincaid_score.append(evaluation_dict[key]['readability_scores']['Kincaid'])
            LIX_score.append(evaluation_dict[key]['readability_scores']['LIX'])
            RIX_score.append(evaluation_dict[key]['readability_scores']['RIX'])
            SMOGIndex_score.append(evaluation_dict[key]['readability_scores']['SMOGIndex'])

            #Calculation dish extraction recall
            dish_extraction_recall.append(len(predicted_dishname) / len(actual_dishname))

            #Calculating sentiment extraction recall
            count = 0
            for i in range(len(actual_sentiment)):
                if actual_sentiment[i] == final_predicted_sentiment[i]:
                    count += 1
                else:
                    continue
            sentiment_extraction_recall.append((count * 1.0) / (len(actual_sentiment) * 1.0))

            #Forming a final dictionary
            temp_review_dict = {
                'Review ID': key,
                'Actual Dishname': ','.join(actual_dishname),
                'Actual Sentiment': ','.join(map(str, actual_sentiment)),
                'Predicted Dishname': ','.join(predicted_dishname),
                'Predicted Sentiment': ','.join(map(str, predicted_sentiment)),
                'Categorical Predicted Sentiment ': ','.join(map(str, final_predicted_sentiment)),
                'ARI': ','.join(map(str, ARI_score)),
                'Coleman-Liau': ','.join(map(str, Coleman_Liu_score)),
                'DaleChallIndex': ','.join(map(str, DaleChallIndex_score)),
                'FleschReadingEase': ','.join(map(str, FleschReadingeEase_score)),
                'GunningFogIndex': ','.join(map(str, GunningFogIndex_score)),
                'Kincaid': ','.join(map(str, Kincaid_score)),
                'LIX': ','.join(map(str, LIX_score)),
                'RIX': ','.join(map(str, RIX_score)),
                'SMOGIndex': ','.join(map(str, SMOGIndex_score)),
                'Dish extraction recall': ','.join(map(str, dish_extraction_recall)),
                'Sentiment extraction recall': ','.join(map(str, sentiment_extraction_recall))
            }
            # Appending for different review IDs
            final_dictionary_list.append(temp_review_dict)

        return final_dictionary_list

    @staticmethod
    def run(filepath):
        with open(filepath, 'rb') as fp:
            evaluation_dict = pickle.load(fp)
            final_dictionary_list = Evaluation.output_scores(evaluation_dict)

        # Save the overall list of dictionaries into a csv output file
        output_filepath = '../output/' + filepath[filepath.rfind('/') + 1:filepath.rfind('.p')] + '_output.csv'
        keys = final_dictionary_list[0].keys()
        with open(output_filepath, 'w', encoding='utf8', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(final_dictionary_list)

Evaluation.run('../output/test_sample.p')
