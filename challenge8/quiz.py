"""
Create a quiz game that generates random questions
and scores the user at the end.

The program should:
    (1) Greet the user, asks their name and store it
    (2) Ask the user how many questions they want and store
        it
    (3) Use the API at https://opentdb.com/api_config.php
        to generate a quiz of up to 10 questions (asks the
        user how many they want)
    (4) Create a menu system for the user to answer the
        questions
    (5) If the user scores less than 75%, insult them using:
        https://insult.mattbas.org/api/insult

The program has been partially written for you.  Complete it!

HINTS

    - Create a new virtual environment and install the
      requests library
    - Experiment with the structured data returned by
      the get_questions() function in the Python interpreter
      to work out how to extract the data you want
    - Build out the get_answer function
    - Use similar code to that provided in the get_questions
      function to query the Insult API for a random insult
    - Write the main program and utilise the functions to
      complete the task
"""

import json
import requests


def get_questions(n):
    """Gets n questions from the Open Trivia Database API"""
    try:
        response = requests.get(f"https://opentdb.com/api.php?amount={n}")
        # JSON RESPONSE SHOULD LOOK SOMEETHING LIKE THIS:
        # {
        #     "response_code": 0,
        #     "results": [
        #         {
        #             "category": "Entertainment: Video Games",
        #             "type": "multiple",
        #             "difficulty": "medium",
        #             "question": "When Halo 3: ODST was unveiled in 2008, it had a different title. What was the game formally called?",
        #             "correct_answer": "Halo 3: Recon",
        #             "incorrect_answers": [
        #                 "Halo 3: Helljumpers",
        #                 "Halo 3: Phantom",
        #                 "Halo 3: Guerilla"
        #             ]
        #         },
        #         .
        #         {{ MORE QUESTIONS }}
        #         .
        #     ]
        # }
        return json.loads(response.content)
    except Exception as e:
        print(f"Fatal Error - Failed to load questions: {e}")
        exit(1)


def get_answer(question, correct_answer, incorrect_answers):
    """Renders the question and possible answers, then takes the user's answer and returs True if it is correct or False if it is not"""


def get_insult():
    """Gets an insult from Matt Bas's Insult API"""
