from nltk.tokenize import sent_tokenize
import spacy
nlp = spacy.load("en_core_web_sm")

class SentenceTokenization:

    @staticmethod
    def get_sentence_tokens(text, module='spacy'):
        sentences = []

        sentence_tokens = []
        if module == 'spacy':
            doc = nlp(text)
            # Feed line by line to the client to detect dish names
            for sentence_token in doc.sents:
                sentence_tokens.append(sentence_token.text)
        elif module == 'nlp':
            sentence_tokens = sent_tokenize(text)
        else:
            sentence_tokens = text.split('.')

        for i in range(len(sentence_tokens)):
            sentence = sentence_tokens[i]
            if sentence != '':
                sentences.append(sentence)

        return sentences