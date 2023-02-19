#!/usr/bin/env python
# ------------------------------------------------------------- #
#                       Justin Powell                           #
#                        02-19-2023                             #
#              Based on 100-day challenge quiz                  #
#   Questions are all from https://opentdb.com/api_config.php   #
# ------------------------------------------------------------- #

from Classes.QuestionGenerator import MakeQuestionBank
from Classes.QuizLogic import QuizLogic

questions = MakeQuestionBank()
quiz = QuizLogic(questions.question_bank)

while quiz.quiz_continue():
    quiz.next_question()

print(":This quiz is over:")
print(f"You got {int(((quiz.score/quiz.question_number)*100))}% correct!")
if (quiz.score / quiz.question_number) < 0.8:
    print("I bet you can do better...")
else:
    print("Great work!")