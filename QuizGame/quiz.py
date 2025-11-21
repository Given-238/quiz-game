import random

# ---------------------------
# QUIZ QUESTIONS (editable)
# ---------------------------

questions = [
    {
        "question": "What is the capital of South Africa?",
        "options": ["Pretoria", "Johannesburg", "Cape Town", "Durban"],
        "answer": "Pretoria"
    },
    {
        "question": "What is 12 x 8?",
               "options": ["86", "96", "108", "112"],
        "answer": "96"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who created the Python programming language?",
        "options": ["James Gosling", "Guido van Rossum", "Elon Musk", "Bill Gates"],
        "answer": "Guido van Rossum"
    }
]

# ---------------------------
# FUNCTIONS
# ---------------------------

def run_quiz():
    score = 0
    random.shuffle(questions)  # randomizes the order
    
    print("\n🧠 WELCOME TO THE QUIZ GAME! 🧠")
    print("Answer the questions by typing the option number.\n")
    
    for q in questions:
        print(q["question"])
        
        # print numbered options
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        
        user_input = input("Your answer (1-4): ")
        
        # validate input
        if not user_input.isdigit() or not (1 <= int(user_input) <= 4):
            print("Invalid input. Question skipped.\n")
            continue
        
        chosen = q["options"][int(user_input) - 1]
        
        if chosen == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌ | Correct answer: {q['answer']}\n")
    
    print("🎯 QUIZ COMPLETE!")
    print(f"Your final score: {score}/{len(questions)}")

    save_score(score)


def save_score(score):
    with open("score.txt", "a") as file:
        file.write(f"Score: {score}/{len(questions)}\n")
    
    print("Your score has been saved to score.txt\n")


# ---------------------------
# START
# ---------------------------

run_quiz()