import html
import json
from urllib.request import urlopen
from os import system
from random import randint

class MakeQuestionBank:
    def __init__(self):
        self.question_bank = self.create_question_bank()

    def generate_url(self):
        quiz_topics = {
            "General": 9,
            "Books": 10,
            "Film": 11,
            "Music": 12,
            "Theatres": 13,
            "Television": 14,
            "Video Games": 15,
            "Board Games": 16,
            "Science": 17,
            "Computers": 18,
            "Mathematics": 19,
            "Mythology": 20,
            "Sports": 21,
            "Geography": 22,
            "History": 23,
            "Politics": 24,
            "Art": 25,
            "Celebrities": 26,
            "Animals": 27,
            "Vehicles": 28,
            "Comics": 29,
            "Gadgets": 30,
            "Cartoons": 31,
            "Anime": 32,
        }
        try:
            num_of_questions = int(input("How many questions would you like?\n"))
        except:
            print("Invalid Response, using default")
            num_of_questions = 10
        question_difficulty = input("Select the difficulty (easy/medium/hard).\n")
        if question_difficulty != "easy" or question_difficulty != "medium" or question_difficulty != "hard":
            question_difficulty = "medium"
        system('clear')
        print(":Available Topics:")
        for key in quiz_topics:
            print(key)
        question_topic = input("Select a topic or leave blank for random (Spelling Matters)\n")
        try:
            topic = quiz_topics[question_topic]
        except:
            topic = randint(9, 32)
        url = f'https://opentdb.com/api.php?amount={num_of_questions}&category={topic}' \
              f'&difficulty={question_difficulty}&type=boolean'
        system('clear')
        return url

    def create_question_bank(self):
        question_bank = []
        response = urlopen(self.generate_url())
        data_json = json.loads(response.read())
        for key in range(0, len(data_json['results'])):
            question = html.unescape(data_json['results'][key]['question'])
            answer = html.unescape(data_json['results'][key]['correct_answer'])
            challenge = {'question': question, 'answer': answer}
            question_bank.append(challenge)
        return question_bank