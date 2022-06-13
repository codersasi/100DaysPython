from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    q = Question(q_text, q_answer)
    question_bank.append(q)

quiz = QuizBrain(question_bank)
while quiz.still_next_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was : {quiz.user_score}/{quiz.question_number}")