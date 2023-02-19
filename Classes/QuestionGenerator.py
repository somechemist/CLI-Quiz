import html
import json
from urllib.request import urlopen
from os import system

class MakeQuestionBank:
    def __init__(self):
        self.question_bank = self.create_question_bank()

    def generate_url(self):
        try:
            num_of_questions = int(input("How many questions would you like?\n"))
        except:
            print("Invalid Response, using default")
            num_of_questions = 10
        question_difficulty = input("Select the difficulty (easy/medium/hard).\n")
        if question_difficulty != "easy" or question_difficulty != "medium" or question_difficulty != "hard":
            question_difficulty = "medium"
        question_topic = input("Select the topic (computers/sports/history/GENERAL)\n")
        if question_topic == "sports":
            topic = 21
        elif question_topic == "computers":
            topic = 18
        elif question_topic == "history":
            topic = 23
        else:
            topic = 9
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