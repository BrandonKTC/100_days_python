from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    answer = quiz_brain.next_question()
    play = quiz_brain.check_answer(answer)
    if play == False:
        break
