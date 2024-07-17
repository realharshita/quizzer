import tkinter as tk
from tkinter import messagebox

class QuizBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bot")
        self.root.geometry("400x300")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the color of the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"}
        ]
        self.current_question = 0
        self.score = 0
        self.time_left = 10

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}s", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 12), command=self.restart_quiz)
        self.restart_button.pack(pady=10)

        self.load_question()
        self.update_timer()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.buttons[i].config(text=option)
            self.time_left = 10
            self.update_timer()
        else:
            self.show_score()

    def check_answer(self, index):
        question_data = self.questions[self.current_question]
        if question_data["options"][index] == question_data["answer"]:
            self.score += 1
        self.current_question += 1
        self.load_question()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score is {self.score} out of {len(self.questions)}")
        self.root.quit()

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.load_question()

root = tk.Tk()
quiz_bot = QuizBot(root)
root.mainloop()
