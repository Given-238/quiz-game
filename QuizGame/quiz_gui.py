import tkinter as tk
import random
import threading
import time

# -------------------------------
# LOAD QUESTIONS FROM FILE
# -------------------------------

def load_questions(filename="questions.txt"):
    questions = {
        "EASY": [],
        "MEDIUM": [],
        "HARD": []
    }

    with open(filename, "r", encoding="utf-8") as f:
        blocks = f.read().strip().split("\n\n")

    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 4:
            continue

        difficulty = lines[0].strip()
        question = lines[1].replace("Q: ", "").strip()
        answer = lines[2].replace("A: ", "").strip()
        options = lines[3].replace("OPTIONS: ", "").split(", ")

        if difficulty in questions:
            questions[difficulty].append({
                "question": question,
                "options": options,
                "answer": answer
            })

    return questions


# -------------------------------
# GUI QUIZ CLASS
# -------------------------------

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.root.config(bg="white")

        self.question_bank = load_questions()
        self.difficulty = None
        self.questions = []
        self.index = 0
        self.score = 0
        self.timer_running = False
        self.time_left = 10

        self.create_difficulty_screen()

    # -------------------------------
    # DIFFICULTY SELECTION
    # -------------------------------

    def create_difficulty_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Choose Difficulty",
                 font=("Arial", 20), bg="white").pack(pady=20)

        tk.Button(self.root, text="Easy", font=("Arial", 16),
                  command=lambda: self.start_quiz("EASY")).pack(pady=10)

        tk.Button(self.root, text="Medium", font=("Arial", 16),
                  command=lambda: self.start_quiz("MEDIUM")).pack(pady=10)

        tk.Button(self.root, text="Hard", font=("Arial", 16),
                  command=lambda: self.start_quiz("HARD")).pack(pady=10)

    # -------------------------------
    # QUIZ START
    # -------------------------------

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.questions = self.question_bank[difficulty]
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0

        self.show_question()

    # -------------------------------
    # DISPLAY A QUESTION
    # -------------------------------

    def show_question(self):
        self.clear_screen()

        if self.index >= len(self.questions):
            self.show_final_score()
            return

        q = self.questions[self.index]

        self.time_left = 10
        self.timer_running = True

        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}",
                                    font=("Arial", 16), fg="red", bg="white")
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=q["question"],
                                       font=("Arial", 18), bg="white", wraplength=500)
        self.question_label.pack(pady=20)

        self.option_buttons = []

        for i, option in enumerate(q["options"]):
            btn = tk.Button(
                self.root,
                text=option,
                font=("Arial", 14),
                width=30,
                command=lambda opt=option: self.check_answer(opt)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.update_timer()

    # -------------------------------
    # TIMER FUNCTION
    # -------------------------------

    def update_timer(self):
        if not self.timer_running:
            return

        if self.time_left <= 0:
            self.timer_running = False
            self.index += 1
            self.show_question()
            return

        self.timer_label.config(text=f"Time Left: {self.time_left}")
        self.time_left -= 1

        self.root.after(1000, self.update_timer)

    # -------------------------------
    # ANSWER CHECKING
    # -------------------------------

    def check_answer(self, selected):
        correct = self.questions[self.index]["answer"]

        if selected == correct:
            self.score += 1

        self.timer_running = False
        self.index += 1
        self.show_question()

    # -------------------------------
    # FINAL SCORE SCREEN
    # -------------------------------

    def show_final_score(self):
        self.clear_screen()

        tk.Label(self.root, text="Quiz Complete!",
                 font=("Arial", 22), bg="white").pack(pady=20)

        tk.Label(self.root, text=f"Your Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 18), bg="white").pack(pady=20)

        tk.Button(self.root, text="Play Again",
                  font=("Arial", 16),
                  command=self.create_difficulty_screen).pack(pady=15)

    # -------------------------------
    # CLEAR SCREEN HELPER
    # -------------------------------

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# -------------------------------
# MAIN LOOP
# -------------------------------

root = tk.Tk()
app = QuizApp(root)
root.mainloop()