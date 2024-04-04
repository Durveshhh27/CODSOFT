import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin", "Rome"], "correct": "Paris"},
            {"question": "What is 2 + 2?", "answers": ["3", "4", "5", "6"], "correct": "4"},
            {"question": "Who is the author of 'Harry Potter' series?", "answers": ["J.K. Rowling", "Stephen King", "George R.R. Martin", "Dan Brown"], "correct": "J.K. Rowling"}
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 12), wraplength=400)
        self.question_label.pack()

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Arial", 10), command=lambda i=i: self.check_answer(self.questions[self.current_question]["answers"][i]))
            button.pack(fill="both", expand=True)
            self.answer_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, answer in enumerate(question_data["answers"]):
                self.answer_buttons[i].config(text=answer)
            self.current_question += 1
        else:
            self.show_score()

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question - 1]["correct"]
        if selected_answer == correct_answer:
            self.score += 1
        self.next_question()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"You have completed the quiz!\nYour score: {self.score}/{len(self.questions)}")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
