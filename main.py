from question_model import Question
from data import question_data
from quiz_brain import Quiz

#create an empty list to store the questions
question_bank = []

#create new questions using the Question method in question_model
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    #append the new questions to the question_bank
    question_bank.append(new_question)

#create a new instance of the class Quiz 
new_quiz = Quiz(question_bank)

#continue until there are questions in the question data
while new_quiz.still_has_question():
    new_quiz.next_question()

#tell the user their score and the total questions attempted
print(f"You've completed the quiz. Your final score is: {new_quiz.score}/{new_quiz.question_number}")
