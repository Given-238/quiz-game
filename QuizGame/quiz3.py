import random
import threading
import time

# ---------------------------
# QUESTION BANK — grouped by difficulty
# ---------------------------

easy_questions = [
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "14"],
        "answer": "12"
    },
    {
        "question": "Which shape has 3 sides?",
        "options": ["Square", "Triangle", "Circle", "Hexagon"],
        "answer": "Triangle"
    }
]

medium_questions = [
    {
        "question": "What is the capital of South Africa?",
        "options": ["Pretoria", "Johannesburg", "Cape Town", "Durban"],
        "answer": "Pretoria"
    },
    {
        "question": "12 × 8 = ?",
        "options": ["96", "108", "112", "86"],
        "answer": "96"
    }
]

hard_questions = [
    {
        "question": "Who created Python?",
        "options": ["Guido van Rossum", "James Gosling", "Linus Torvalds", "Bill Gates"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    }
]

# ----------------------------------------------------
# SELECT DIFFICULTY
# ----------------------------------------------------

def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("\nEnter 1, 2, or 3: ")
    
    if choice == "1":
        return easy_questions
    elif choice == "2":
        return medium_questions
    elif choice == "3":
        return hard_questions
    else:
        print("Invalid choice, defaulting to Medium.")
        return medium_questions


# ----------------------------------------------------
# INPUT WITH TIMER (10 seconds)
# ----------------------------------------------------

user_answer = None

def get_input():
    global user_answer
    user_answer = input("Your answer (1-4): ")

def timed_input(timeout=10):
    global user_answer
    user_answer = None

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    start = time.time()
    while time.time() - start < timeout:
        if user_answer is not None:
            return user_answer
        time.sleep(0.1)

    return None  # timeout reached


# ----------------------------------------------------
# MAIN QUIZ WITH TIMER
# ----------------------------------------------------

def run_quiz():
    questions = choose_difficulty()
    random.shuffle(questions)

    score = 0
    print("\n🧠 WELCOME TO THE QUIZ GAME — TIMED MODE 🧠")
    print("⏳ You have **10 seconds** to answer each question!\n")

    for q in questions:
        print(q["question"])

        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        print("⏳ Timer started!")

        answer = timed_input(timeout=10)

        if answer is None:
            print("⏰ Time's up! You missed the question.\n")
            continue

        if not answer.isdigit() or not (1 <= int(answer) <= 4):
            print("Invalid answer.\n")
            continue

        chosen = q["options"][int(answer) - 1]

        if chosen == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌ | Correct answer: {q['answer']}\n")

    print(f"🎯 FINAL SCORE: {score}/{len(questions)}")
    save_score(score, len(questions))


# ----------------------------------------------------
# SAVE SCORE
# ----------------------------------------------------

def save_score(score, total):
    with open("score.txt", "a") as f:
        f.write(f"Score: {score}/{total}\n")
    print("Score saved to score.txt\n")


# ----------------------------------------------------
# PROGRAM START
# ----------------------------------------------------

run_quiz()