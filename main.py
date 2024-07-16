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

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.buttons[i].config(text=option)
        else:
            self.show_score()

root = tk.Tk()
quiz_bot = QuizBot(root)
root.mainloop()