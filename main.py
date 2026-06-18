

# print("Welcome to the German Vocabulary Quizz App.")
#
# print("You will be quizzed on 5 different words, each one is harder than the next. You also get 3 attempts at each word. Good luck!")
#
# is_ready= input("are you ready? Yes or No.\n").lower().strip()
# if is_ready == "yes":
#     print("Let's start")
#     W1_correct = False
#
#     score = 0
#     lives = 3
#     while W1_correct == False and lives > 0:
#         W1 = input("What does 'Gesund' mean? Health or Life.\n").lower().strip()
#
#         if W1 == "health":
#             score += 1
#             print(f"Well done. You scored. Your corrent score is {score}.")
#             W1_correct = True
#
#         else:
#             lives -= 1
#             if lives > 0:
#                 suffix = "attempt" if lives == 1 else "attempts"
#                 print(f"Incorrect answer. Try again. You still have {lives} {suffix} left.")
#             else:
#                 print(f"Sorry. You ran out of lives. You total score so far is {score}. Next question. ")
#     W2_correct = False
#     lives = 3
#     while W2_correct == False and lives > 0:
#
#         W2 = input("What does the word 'Günstige' mean? expensive or affordable.\n").lower().strip()
#
#         if W2 == "affordable":
#             score += 1
#             print(f"Great job. You scored again. Your current score is {score}.")
#             W2_correct = True
#
#         else:
#             lives -= 1
#             if lives > 0:
#                 suffix = "attempt" if lives == 1 else "attempts"
#                 print(f"Incorrect answer. Try again. You still have {lives} {suffix} left.")
#             else:
#                 print(f"Sorry. You ran out of lives. You total score so far is {score}. Next question. ")
#     W3_correct = False
#     lives = 3
#     while W3_correct == False and lives >0:
#         W3 = input("What does the word 'Schwierigkeiten' mean? difficulties or opportunities.\n").lower().strip()
#         if W3 == "difficulties":
#             score += 1
#             print(f"Excellent job. Your current score is {score}")
#             W3_correct = True
#
#         else:
#             lives -= 1
#             if lives > 0:
#                 suffix = "attempt" if lives == 1 else "attempts"
#                 print(f"Incorrect answer. Try again. You still have {lives} {suffix} left.")
#             else:
#                 print(f"Sorry. You ran out of lives. You total score so far is {score}. Next question. ")
#     W4_correct = False
#     lives = 3
#     while W4_correct == False and lives > 0:
#         W4 = input("What does the word 'Aufmerksamkeit' mean? necessary or awareness.\n").lower().strip()
#         if W4 == "awareness":
#             score += 1
#             print(f"Awesome. Your current score is {score}")
#             W4_correct = True
#
#         else:
#             lives -= 1
#             if lives > 0:
#                 suffix = "attempt" if lives == 1 else "attempts"
#                 print(f"Incorrect answer. Try again. You still have {lives} {suffix} left.")
#             else:
#                 print(f"Sorry. You ran out of lives. You total score so far is {score}. Next question. ")
#     W5_correct = False
#     lives = 3
#     while W5_correct == False and lives > 0:
#         W5 = input("Which word means necessary? 'nöstig' or 'schaffen'.\n").lower().strip()
#         if W5 == "nöstig":
#             score += 1
#             print(f"Nailed it. Your current score is {score}")
#             W5_correct = True
#
#         else:
#             lives -= 1
#             if lives > 0:
#                 suffix = "attempt" if lives == 1 else "attempts"
#                 print(f"Incorrect answer. Try again. You still have {lives} {suffix} left.")
#             else:
#                 print(f"Sorry. You ran out of lives. You total score so far is {score}. Next question. ")
# else:
#     print("Whenever you are ready then.")

#space at the end of answers renders answer incorrect. SOLVED
#need total score to show after each answer, correct or not. SOLVED
#user answer better be on the next line and not right next to the question, or at least add in some space. SOLVED
#when answer is wrong, let's give the user the chance to try again before moving to the next question. SOLVED
#after the third attempt, it should stop saying you have {lives} since it's now 0. SOLVED
#when it gets to 1, it should remove the 's' from attempts. SOLVED

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
        if not game_over != True:
            print(f"{RED} Game Over. {RESET}")
            break
else:
    print("Whenever you are ready then.")


#bug_1: score not updated. SOLVED
#bug_2: when user runs out of lives, total score is 0 for some reason. SOLVED
#bug_3: need space (\n). SOLVED
#bug_4: adding space at the end renders answer wrong. SOLVED
#bug_5: spacing issue with input. SOLVED
#02/06
#bug_6: when running outta life, user still gets to move on to the next question!!!
# How about take off a point and maybe end the game;) SOLVED
#bug_7: this dictionary for loop is noice, what if one or more questions have different format, what if instead of choice, user gotta write. SOLVED.
#bug_8: can we tolerate minor spelling issues, missing an s or a letter = still acceptable??