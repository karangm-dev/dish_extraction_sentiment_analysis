import pickle
import pprint
pp = pprint.PrettyPrinter(width=200, compact=True)

class Check:
    @staticmethod
    def run(filepath):
        with open(filepath, 'rb') as fp:
            evaluation_dict = pickle.load(fp)
            pp.pprint(evaluation_dict['_xz2yV-x77sJgaE6flSItw'])

Check.run('../output/test_3.p')