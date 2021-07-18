from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_BACKGROUND = "#fff"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.lbl_score = Label(
            text=f"Score: {self.quiz.score}",
            font=("Arial", 12, "bold"),
            highlightbackground=THEME_COLOR,
            background=THEME_COLOR,
            bd=0,
        )
        self.lbl_score.grid(row=0, column=1, padx=20, pady=20)

        # Question
        self.question = Canvas(
            width=300,
            height=250,
            highlightbackground=QUESTION_BACKGROUND,
            background=QUESTION_BACKGROUND,
            bd=0,
        )
        self.question_text = self.question.create_text(
            150, 125, font=("Arial", 20, "italic"), width=280
        )
        self.question.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Button Check
        self.img_check = PhotoImage(file="./images/true.png")
        self.btn_check = Button(
            image=self.img_check,
            highlightbackground=THEME_COLOR,
            background=THEME_COLOR,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.true_pressed,
        )
        self.btn_check.grid(row=2, column=0, padx=20, pady=20)

        # Button Cross
        self.img_cross = PhotoImage(file="./images/false.png")
        self.btn_cross = Button(
            image=self.img_cross,
            highlightbackground=THEME_COLOR,
            background=THEME_COLOR,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.false_pressed,
        )
        self.btn_cross.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question.config(bg=QUESTION_BACKGROUND)
            self.question.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.question.config(bg=QUESTION_BACKGROUND)
            self.question.itemconfig(self.question_text, text=f"You've completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.btn_check.config(state="disabled")
            self.btn_cross.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question.config(bg="green")
            self.update_score()
        else:
            self.question.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.lbl_score.config(text=f"Score: {self.quiz.score}")
