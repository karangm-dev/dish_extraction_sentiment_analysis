from entity import SEntity
import pandas as pd

class EntityApp:

    def __init__(self):
        self.__sentity = SEntity()

    def create_entity(self):
        # Load the menu item
        menu_df = pd.read_csv("../input/CheeseCakeFactory-Menu.csv")
        value_synonym_map = {}
        for index, row in menu_df.iterrows():
            menu_item = row['Dish Name']
            value_synonym_map[menu_item] = [menu_item]

        response = self.__sentity.create("Menu", value_synonym_map, enable_fuzzy_extraction=True)
        print(response)
        # result = sentity.list()
        # print(result)

    def run(self):
        self.create_entity()


entity_app = EntityApp()
entity_app.run()