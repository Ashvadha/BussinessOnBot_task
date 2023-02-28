# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import operator

class ActionMathOperation(Action):

    def name(self) -> Text:
        return "action_math_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extracting entities from the user input
        num1 = int(tracker.get_slot("num1"))
        num2 = int(tracker.get_slot("num2"))
        op = tracker.get_slot("operator")
        
        # Perform the corresponding mathematical operation based on the operator
        if op == '+':
            result = operator.add(num1, num2)
        elif op == '-':
            result = operator.sub(num1, num2)
        elif op == '*':
            result = operator.mul(num1, num2)
        elif op == '/':
            if num2!= 0:
                result = operator.truediv(num1, num2)
            else :
                result = "Can't divide by 0"
        else:
            result = "Invalid operator"

        # Send the result to the user
        dispatcher.utter_message(template="utter_math_result", result=result)

        return []