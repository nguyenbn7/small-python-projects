import random
from os import path, makedirs

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

BASE_DIR = path.dirname(path.abspath(__file__))
quizzes_dir = path.join(BASE_DIR, "quizzes")
makedirs(quizzes_dir, exist_ok=True)
quiz_answers_dir = path.join(BASE_DIR, "quiz_answers")
makedirs(quiz_answers_dir, exist_ok=True)

for quiz_num in range(35):
    with open(
        path.join(quizzes_dir, f"capitalsquiz{quiz_num + 1}.txt"), "w"
    ) as quiz_file:
        with open(
            path.join(quiz_answers_dir, f"capitalsquiz_answers{quiz_num + 1}.txt"), "w"
        ) as answer_key_file:
            # Write out the header for the quiz.
            quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
            quiz_file.write((" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})")
            quiz_file.write("\n\n")

            # Shuffle the order of the states.
            states = list(capitals.keys())
            random.shuffle(states)

            for question_num in range(len(capitals)):
                correct_answer = capitals[states[question_num]]
                wrong_answers = list(capitals.values())

                del wrong_answers[wrong_answers.index(correct_answer)]
                wrong_answers = random.sample(wrong_answers, 3)
                answer_options = wrong_answers + [correct_answer]
                random.shuffle(answer_options)

                quiz_file.write(
                    f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
                )
                for i, answer in enumerate(answer_options):
                    quiz_file.write(f"    {'ABCD'[i]}. {answer}\n")
                quiz_file.write("\n")

                answer_key_file.write(
                    f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n"
                )
