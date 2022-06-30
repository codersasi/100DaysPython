from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", width=275, font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_correct)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_wrong)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state=NORMAL)
            self.false_button.config(state=NORMAL)
        else:
            self.canvas.itemconfig(self.question_text, text="The End")

    def answer_correct(self):
        self.check_and_update_score("True")

    def answer_wrong(self):
        self.check_and_update_score("False")

    def check_and_update_score(self, user_answer):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        is_correct_answer = self.quiz.check_answer(user_answer)
        canvas_color = "red"
        if is_correct_answer:
            canvas_color = "green"
            self.score_label.config(text=f"Score : {self.quiz.score}")

        self.canvas.config(bg=canvas_color)
        self.window.after(2000, self.ui_feedback)

    def ui_feedback(self):
        self.canvas.config(bg="white")
        self.get_next_question()