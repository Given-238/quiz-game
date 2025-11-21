import random
import threading
import time

# ----------------------------------------------------
# GLOBALS FOR TIMER
# ----------------------------------------------------
user_answer = None


# ----------------------------------------------------
# LOAD QUESTIONS FROM TEXT FILE
# ----------------------------------------------------

def load_questions(filename="questions.txt"):
    questions = {
        "EASY": [],
        "MEDIUM": [],
        "HARD": []
    }

    with open(filename, "r", encoding="utf-8") as f:
        data = f.read().strip().split("\n\n")  # separate blocks

    for block in data:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue  # skip empty lines

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


# ----------------------------------------------------
# CHOOSE DIFFICULTY
# ----------------------------------------------------

def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("\nEnter 1, 2, or 3: ")
    
    if choice == "1": return "EASY"
    if choice == "2": return "MEDIUM"
    if choice == "3": return "HARD"

    print("Invalid choice. Defaulting to MEDIUM.")
    return "MEDIUM"


# ----------------------------------------------------
# TIMED INPUT FOR 10 SECONDS
# ----------------------------------------------------

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

    return None


# ----------------------------------------------------
# MAIN QUIZ FUNCTION
# ----------------------------------------------------

def run_quiz():
    difficulty = choose_difficulty()
    question_bank = load_questions()
    questions = question_bank[difficulty]

    random.shuffle(questions)
    score = 0

    print("\n🧠 QUIZ GAME — Questions Loaded From File 🧠")
    print("⏳ You have 10 seconds per question!\n")

    for q in questions:
        print(q["question"])

        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        print("⏳ Timer started!")

        answer = timed_input(timeout=10)

        if answer is None:
            print("⏰ Time's up!\n")
            continue

        if not answer.isdigit() or not (1 <= int(answer) <= 4):
            print("Invalid answer.\n")
            continue

        chosen = q["options"][int(answer) - 1]

        if chosen == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌ | Correct: {q['answer']}\n")

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