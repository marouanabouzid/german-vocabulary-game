

GREEN = "\033[1;32;40m"
RED = "\033[1;31;40m"
YELLOW = "\033[1;33;40m"
RESET = "\033[0m"
quiz_questions = [
    {
        "german_word": "Gesund",
        "choices": "Health or Life",
        "correct_answer": "health",
        "format": "multiple_choice"
    },
    {
        "german_word": "Günstige",
        "choices": "expensive or affordable",
        "correct_answer": "affordable",
        "format": "multiple_choice"

    },
    {
        "german_word": "Schwierigkeiten",
        "choices": "difficulties or opportunities",
        "correct_answer": "difficulties",
        "format": "multiple_choice"
    },
    {
        "german_word": "Aufmerksamkeit",
        "choices": "necessary or awareness",
        "correct_answer": "awareness",
        "format": "multiple_choice"
    },
    {
        "german_word": "useful",
        "choices": "schaffen or nützlich",
        "correct_answer": "nützlich",
        "format": "multiple_choice"
    },
    {
        "german_word": "Verwenden",
        "correct_answer": "apply",
        "format": "write"
    }
]
print("Welcome to the German Vocabulary Quizz App.")

print("You will be quizzed on 5 different words, each one is harder than the next. You also get 3 attempts at each word. Good luck!")

is_ready= input("are you ready? Yes or No.\n").lower().strip()
game_over = False
if is_ready == "yes":
    print("Let's start")
    score = 0

    for question in quiz_questions:
        lives = 3
        correct = False
        while correct == False and lives > 0:
            if question['format'] == 'write':
                user_input = input(f"What does '{question['german_word']}' mean?\n").lower().strip()
            else:
                user_input = input(f"What does '{question['german_word']}' mean? {question['choices']} \n").lower().strip()
            if user_input == question['correct_answer']:
                score += 1
                correct = True
                print(f"{GREEN}Correct! Your current score is {score} {RESET}")
            else:
                lives -=1
                if lives > 0:
                    suffix = "attempt" if lives == 1 else "attempts"
                    print(f"{YELLOW}Incorrect answer. Try again. You still have {lives} {suffix} left.{RESET}")
                else:
                    game_over = True
                    score -=1
                    print(f"Sorry you ran out of lives. Minus 1 point. Your total score so far is {score}")
    if not game_over:
        print(f"{GREEN} Congratulation! You mastered all five words! Final score is {score}/ {len(quiz_questions)} {RESET}")
    if not game_over != True:
        print(f"{RED} Game Over. {RESET}")

else:
    print("Whenever you are ready then.")
