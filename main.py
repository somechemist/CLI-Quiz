from Classes.QuestionGenerator import MakeQuestionBank
from Classes.QuizLogic import QuizLogic

questions = MakeQuestionBank()
# print(len(quiz.question_bank))
# for key in range(0, len(quiz.question_bank)):
#     print(quiz.question_bank[key]['question'])
quiz = QuizLogic(questions.question_bank)

while quiz.quiz_continue():
    quiz.next_question()

print("The quiz is over")
print(f"Your score was {quiz.score}/{quiz.question_number}")