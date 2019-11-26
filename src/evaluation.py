import pickle
import pprint
pp = pprint.PrettyPrinter(width=200, compact=True)

class Evaluation:

    @staticmethod
    def run(filepath):
        with open(filepath, 'rb') as fp:
            evaluation_dict = pickle.load(fp)
            pp.pprint(evaluation_dict)

Evaluation.run('../output/test_sample.p')
