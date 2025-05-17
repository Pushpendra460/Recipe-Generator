from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionGetRecipe(Action):
    def name(self) -> Text:
        return "action_get_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message.get('text').lower()

        with open("recipes_dataset.json", "r") as file:
            data = json.load(file)

        found = None
        for key in data:
            if key in text:
                found = key
                break

        if found:
            recipe = data[found]
            message = f"🍽️ Recipe for {found.capitalize()}:\nIngredients: {', '.join(recipe['ingredients'])}\nInstructions: {recipe['instructions']}"
        else:
            message = "❌ Sorry, I don't have that recipe yet."

        dispatcher.utter_message(text=message)
        return []
