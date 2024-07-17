import tkinter as tk
from tkinter import messagebox
import random
import winsound

class QuizBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bot")
        self.root.geometry("400x400")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the color of the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "answer": "Harper Lee"},
            {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Saturn", "Earth", "Mars"], "answer": "Jupiter"}
        ]
        random.shuffle(self.questions)
        for question in self.questions:
            random.shuffle(question["options"])

        self.current_question = 0
        self.score = 0
        self.time_left = 10

        self.welcome_screen()

    def welcome_screen(self):
        self.clear_screen()
        welcome_label = tk.Label(self.root, text="Welcome to the Quiz Bot!", font=("Helvetica", 18))
        welcome_label.pack(pady=20)

        instructions_label = tk.Label(self.root, text="Answer the questions within the time limit. Click Start to begin.", font=("Helvetica", 12))
        instructions_label.pack(pady=10)

        start_button = tk.Button(self.root, text="Start", font=("Helvetica", 12), command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        self.clear_screen()
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}s", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.progress_label = tk.Label(self.root, text=f"Question 1 of {len(self.questions)}", font=("Helvetica", 12))
        self.progress_label.pack(pady=10)

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
            self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
            self.time_left = 10
            self.update_timer()
        else:
            self.show_summary()

    def check_answer(self, index):
        question_data = self.questions[self.current_question]
        if index == -1 or question_data["options"][index] != question_data["answer"]:
            correct_index = question_data["options"].index(question_data["answer"])
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            messagebox.showinfo("Incorrect", f"Correct answer: {question_data['answer']}")
        else:
            self.score += 1
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        self.current_question += 1
        self.load_question()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    def show_summary(self):
        self.clear_screen()
        summary_label = tk.Label(self.root, text="Quiz Completed", font=("Helvetica", 18))
        summary_label.pack(pady=20)

        score_label = tk.Label(self.root, text=f"Your score is {self.score} out of {len(self.questions)}", font=("Helvetica", 14))
        score_label.pack(pady=10)

        for i, question_data in enumerate(self.questions):
            result_label = tk.Label(self.root, text=f"Q{i+1}: {question_data['question']}\nCorrect answer: {question_data['answer']}", font=("Helvetica", 12))
            result_label.pack(pady=5)

        restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 12), command=self.restart_quiz)
        restart_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def restart_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            random.shuffle(question["options"])
        self.current_question = 0
        self.score = 0
        self.start_quiz()

root = tk.Tk()
quiz_bot = QuizBot(root)
root.mainloop()
