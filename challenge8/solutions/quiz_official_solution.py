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
        https://insult.mattbas.org/api/

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

import html
import json
import random
import requests


def get_questions(n):
    """Gets n questions from the Open Trivia Database API"""
    response = requests.get(f"https://opentdb.com/api.php?amount={n}")
    # JSON RESPONSE SHOULD LOOK SOMETHING LIKE THIS:
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


def get_answer(question, correct_answer, incorrect_answers):
    """Renders the question and possible answers, then takes the user's answer and returs True if it is correct or False if it is not"""
    # Create a copy of the list containing the worng answers, add the correct
    # answer then shuffle them in to a random order so the correct answer isn't
    # always last.
    answers = incorrect_answers[:]
    answers.append(correct_answer)
    random.shuffle(answers)
    # Generate a menu to display the question and a list of the possible
    # answers.  The API appears to return the questions and answers in strings
    # that escape special characters in HTML, e.g.:
    #   In the &quot;Kagerou Daze&quot; series...
    #
    # This should actually be displayed as:
    #   In the '&quot;'Kagerou Daze' series...
    #
    # Also, leading and trailing spaces occasionally appear so strip them off
    # too
    sanitized_question = html.unescape(question).strip()
    menu = "\n" + sanitized_question + "\n\n"
    valid_answers = []
    for i in range(0, len(answers)):
        sanitized_answer = html.unescape(answers[i]).strip()
        menu += f" [{i}] {sanitized_answer}\n"
        valid_answers.append(str(i))
    # Print the menu and solicit and answer:
    print(menu)
    answer = ""
    while answer not in valid_answers:
        answer = input(
            f"Enter your answer [{valid_answers[0]} - {valid_answers[-1]}]: "
        )
    # Return True if the answer was correct
    if answers[int(answer)] == correct_answer:
        return True
    else:
        return False


def get_insult():
    """Gets an insult from Matt Bas's Insult API"""
    try:
        response = requests.get(f"https://insult.mattbas.org/api/insult.txt")
        # PLAIN TEXT RESPONSE SHOULD LOOK SOMETHING LIKE THIS:
        #
        # You are as pointless as a detrimental yucky load of dreadful pig stench
        if len(response.text) > 0:
            return response.text
    except Exception:
        pass
    # Provide a default insult if the API is not working
    return (
        "I am unable to find an insult that captures your inadequacy (API unavailable)"
    )


# Get the questions from the API and immediatley quit if none are available
try:
    questions = get_questions(3)
    questions = questions["results"]
except Exception as e:
    print(f"Fatal Error - failed to load questions: {e}")
    exit(1)

# Start the quiz - keep a running total of correct answers
correct_answers = 0
for question in questions:
    correct = get_answer(
        question=question["question"],
        correct_answer=question["correct_answer"],
        incorrect_answers=question["incorrect_answers"],
    )
    if correct:
        correct_answers += 1

# Calculate the final score and insult the user as necessary
score_percentage = correct_answers / len(questions) * 100

if score_percentage >= 75:
    print(f"\nWell done! You scored {score_percentage:.0f}%.\n")
else:
    insult = get_insult()
    print(f"\n{insult}. You scored {score_percentage:.0f}%.\n")
