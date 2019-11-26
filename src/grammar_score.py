import readability

class GrammarScore:

    @staticmethod
    def get_scores(text):
        readability_dict = {}
        results = readability.getmeasures(text, lang='en')
        readability_dict['Kincaid'] = results['readability grades']['Kincaid']
        readability_dict['ARI'] = results['readability grades']['ARI']
        readability_dict['Coleman-Liau'] = results['readability grades']['Coleman-Liau']
        readability_dict['FleschReadingEase'] = results['readability grades']['FleschReadingEase']
        readability_dict['GunningFogIndex'] = results['readability grades']['GunningFogIndex']
        readability_dict['LIX'] = results['readability grades']['LIX']
        readability_dict['SMOGIndex'] = results['readability grades']['SMOGIndex']
        readability_dict['RIX'] = results['readability grades']['RIX']
        readability_dict['DaleChallIndex'] = results['readability grades']['DaleChallIndex']

        return readability_dict