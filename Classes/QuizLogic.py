from os import system
from time import sleep
class QuizLogic:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def quiz_continue(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        current = self.question_number
        next = current + 1
        answer = input(f"Q.{next} : {self.question_bank[current]['question']} (True/False)?\n")
        self.question_number = next
        if self.check_answer(answer, self.question_bank[current]['answer']):
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        sleep(2)
        system('clear')

    def check_answer(self, u_answer, c_answer):
        return u_answer == c_answer
