import dialogflow_v2 as dialogflow

class STrainingPhrase:

    def __init__(self):
        self.training_phrases = self.run()

    def get_example_1(self):
        training_sentence = u"This location is in Legacy Village in Lyndhurst. The service is always really good. " \
            u"It's pretty easy to find a parking space. \n\nWhen there is a wait you can walk around the shopping center. " \
            u"There is a Crate & Barrel next door. The pagers work pretty far too.\n\nThe portions are large enough to " \
            u"share. The food is always good and hot and there's something for everyone. \n\nSome of my favorite " \
            u"appetizers are the Roadside Sliders, Southern Fried Chicken Sliders and the Firecracker Salmon. " \
            u"\n\nMy favorite specialties are the Ranch House Burger, Steak Diane and the Grilled Shrimp & Bacon Club. " \
            u"\n\nMy favorite cheesecake is the Dulce De Leche Caramel Cheesecake. It is absolutely amazing! \n\n" \
            u"My favorite drinks are the Tropical Smoothie and the Frozen Iced Mango.\n\nMy only complaint is that " \
            u"they don't offer a kid's menu. But they do offer a complementary baby plate that consists of bananas, " \
            u"oranges and bread."

        parts = [

            dialogflow.types.Intent.Intent.TrainingPhrase.Part(text=
                u"This location is in Legacy Village in Lyndhurst. The service is always really good. " \
                u"It's pretty easy to find a parking space. \n\nWhen there is a wait you can walk around the shopping center. " \
                u"There is a Crate & Barrel next door. The pagers work pretty far too.\n\nThe portions are large enough to " \
                u"share. The food is always good and hot and there's something for everyone. \n\nSome of my favorite " \
                u"appetizers are the Roadside Sliders, Southern Fried Chicken Sliders and the Firecracker Salmon. " \
                u"\n\nMy favorite specialties are the Ranch House Burger, Steak Diane and the Grilled Shrimp & Bacon Club. " \
                u"\n\nMy favorite cheesecake is the Dulce De Leche Caramel Cheesecake. It is absolutely amazing! \n\n" \
                u"My favorite drinks are the Tropical Smoothie and the Frozen Iced Mango.\n\nMy only complaint is that " \
                u"they don't offer a kid's menu. But they do offer a complementary baby plate that consists of bananas, " \
                u"oranges and bread."
            ),
            dialogflow.types.Intent.Intent.TrainingPhrase.Part(text='apples', entity_type='@fruit:fruit')
        ]
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=parts)

        part_1 = dialogflow.types.Intent.TrainingPhrase.Part(text=training_sentence)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part_1])


    # def run(self):
    #     # Training Phrases
    #     training_phrases = []
    #     for training_sentence in training_sentences:
    #
    #         training_phrases.append(training_phrase)
