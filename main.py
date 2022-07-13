from question_model import Question
from data import question_data
from quiz_brain import Quiz


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

new_quiz = Quiz(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

print(f"You've completed the quiz. Your final score is: {new_quiz.score}/{new_quiz.question_number}")