import dialogflow_v2 as dialogflow
from config import Config
from google.protobuf import json_format

class SClient:
    def __init__(self):
        self.client = dialogflow.SessionsClient()

    def detect_intent_for_text(self, text):
        session = self.client.session_path(Config.GOOGLE_PROJECT_ID, Config.SESSION_ID)
        # TODO: Initialize `query_input`:
        text_input = dialogflow.types.TextInput(text=text, language_code='en-US')
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.client.detect_intent(session, query_input)
        intent = response.query_result.intent.display_name
        parameters = json_format.MessageToDict(response.query_result.parameters)
        dish_names = {}
        if 'Menu' in parameters:
            dish_names = parameters['Menu']
        return intent, dish_names

