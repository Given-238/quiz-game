import random

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
# CHOOSE DIFFICULTY FUNCTION
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
        print("Invalid choice, defaulting to Medium difficulty.")
        return medium_questions


# ----------------------------------------------------
# MAIN QUIZ FUNCTION
# ----------------------------------------------------

def run_quiz():
    questions = choose_difficulty()
    random.shuffle(questions)

    score = 0
    print("\n🧠 WELCOME TO THE QUIZ GAME (Difficulty Mode) 🧠\n")

    for q in questions:
        print(q["question"])

        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        user_input = input("Your answer (1-4): ")

        if not user_input.isdigit() or not (1 <= int(user_input) <= 4):
            print("Invalid answer. Skipped.\n")
            continue

        chosen = q["options"][int(user_input) - 1]

        if chosen == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌ | Correct: {q['answer']}\n")

    print(f"🎯 Final Score: {score}/{len(questions)}")
    save_score(score, len(questions))


# ----------------------------------------------------
# SAVE SCORE FUNCTION
# ----------------------------------------------------

def save_score(score, total):
    with open("score.txt", "a") as f:
        f.write(f"Score: {score}/{total}\n")
    print("Score saved to score.txt\n")


# ----------------------------------------------------
# PROGRAM START
# ----------------------------------------------------

run_quiz()