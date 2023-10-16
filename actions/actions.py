# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from rasa_sdk.events import EventType, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict

from actions.DBconnect import DBconnect
from typing import Any, Text, Dict, List


class action_utter_faq(Action):
    def name(self) -> Text:
        return "action_utter_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,) -> List[EventType]:

        full_intent = (
            tracker.latest_message.get("response_selector", {})
            .get("faq", {})
            .get("response", {})
            .get("intent_response_key")
        )
        if full_intent:
            topic = full_intent.split("/")[1]
        else:
            topic = None

        mongo_client = DBconnect()
        response, is_action, url_link, text, img = mongo_client.vyhledat_intent(topic)

        if is_action.lower() in ("true", "1"):
            is_action = True
        else:
            is_action = False

        if is_action:
            dispatcher.utter_message(
                template="utter_custom_response",
                text_response=response,
                img=img,
                url=url_link,
                url_text=text
            )
        else:
            dispatcher.utter_message(
                text=response,
            )

        return []
