# Load your usual SpaCy model (one of SpaCy English models)
import warnings
warnings.filterwarnings('ignore')

import spacy
nlp = spacy.load("en")

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

class CoreferenceResolution:

    @staticmethod
    def run(text):
        doc = nlp(text)
        resolved_text = doc._.coref_resolved
        return resolved_text