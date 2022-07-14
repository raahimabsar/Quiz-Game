class Quiz():
    '''
    structure for the main Quiz
    '''
    def __init__(self,question_list):
        """
        input:
        question_list -- a list of dictionaries with questions as 'texts'
        and answers as 'answers'
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    #check if there are questions left in question_lits
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    #initialize questions from question_lists to current_question chronologically
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #ask user input and check user answer by calling check_answer method
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    #check user's input against the correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")







