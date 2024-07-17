import tkinter as tk
from tkinter import messagebox
import random

class QuizBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bot")
        self.root.geometry("600x400")

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.timer_seconds = 10
        self.username = ""

        self.high_scores = self.load_high_scores()

        self.welcome_screen()

    def welcome_screen(self):
        self.clear_screen()
        welcome_label = tk.Label(self.root, text="Welcome to the Quiz Bot!", font=("Helvetica", 24, "bold"))
        welcome_label.pack(pady=20)

        instructions_label = tk.Label(self.root, text="Enter your name and click Start to begin.", font=("Helvetica", 14))
        instructions_label.pack(pady=10)

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.name_entry.pack(pady=10)

        start_button = tk.Button(self.root, text="Start", font=("Helvetica", 14, "bold"), bg="green", fg="white", command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        self.username = self.name_entry.get()
        if not self.username:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        self.clear_screen()

        self.generate_random_questions()

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 14), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.timer_seconds}s", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.progress_label = tk.Label(self.root, text=f"Question 1 of {len(self.questions)}", font=("Helvetica", 12))
        self.progress_label.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 12), command=self.restart_quiz)
        self.restart_button.pack(pady=10)

        self.load_question()
        self.update_timer()

    def generate_random_questions(self):
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

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.buttons[i].config(text=option, bg="SystemButtonFace", state="normal")
            self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
            self.timer_seconds = 10
            self.update_timer()
        else:
            self.show_summary()

    def check_answer(self, index):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["answer"]

        if index == -1:  # Check if time runs out
            messagebox.showinfo("Time's up!", f"Correct answer: {correct_answer}")
        elif question_data["options"][index] != correct_answer:
            messagebox.showinfo("Incorrect", f"Correct answer: {correct_answer}")
        else:
            self.score += 1

        for i, option in enumerate(question_data["options"]):
            if option == correct_answer:
                self.buttons[i].config(bg="light green")
            else:
                self.buttons[i].config(bg="light coral")

        self.buttons[index].config(state="disabled")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.root.after(1000, self.load_question)
        else:
            self.show_summary()

    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_label.config(text=f"Time left: {self.timer_seconds}s")
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    def show_summary(self):
        self.clear_screen()
        summary_label = tk.Label(self.root, text="Quiz Completed", font=("Helvetica", 24, "bold"))
        summary_label.pack(pady=20)

        score_label = tk.Label(self.root, text=f"Your score is {self.score} out of {len(self.questions)}", font=("Helvetica", 18))
        score_label.pack(pady=10)

        self.update_high_scores()

        for i, question_data in enumerate(self.questions):
            result_label = tk.Label(self.root, text=f"Q{i+1}: {question_data['question']}\nCorrect answer: {question_data['answer']}", font=("Helvetica", 14))
            result_label.pack(pady=5)

        high_scores_label = tk.Label(self.root, text="High Scores:", font=("Helvetica", 18, "bold"))
        high_scores_label.pack(pady=10)

        for score_entry in self.high_scores:
            high_score_label = tk.Label(self.root, text=f"{score_entry['name']}: {score_entry['score']}", font=("Helvetica", 14))
            high_score_label.pack()

        restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 14, "bold"), bg="green", fg="white", command=self.restart_quiz)
        restart_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def restart_quiz(self):
        self.generate_random_questions()
        self.current_question = 0
        self.score = 0
        self.start_quiz()

    def load_high_scores(self):
        return [
            {"name": "Player1", "score": 5},
            {"name": "Player2", "score": 4},
            {"name": "Player3", "score": 3},
            {"name": "Player4", "score": 2},
            {"name": "Player5", "score": 1}
        ]

    def update_high_scores(self):
        self.high_scores.append({"name": self.username, "score": self.score})
        self.high_scores = sorted(self.high_scores, key=lambda x: x["score"], reverse=True)[:5]

root = tk.Tk()
quiz_bot = QuizBot(root)
root.mainloop()
