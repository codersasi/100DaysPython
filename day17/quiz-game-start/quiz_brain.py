class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_next_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's Wrong.")
        print(f"The Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")
