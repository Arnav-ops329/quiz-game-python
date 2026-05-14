# This is the main file that contains the overall logic

from questions import questions  # To access the questions from a different file

print("===== WELCOME TO THE QUIZ GAME =====")
input()
print(
    "Some questions would be displayed and you have to answer them, based on the answers you would be granted with points."
)
input()

score = 0  # To set the score of the user to zero
for q in questions:
    print("\n" + q["Question"])

    for i, options in enumerate(q["Options"], start=1):
        print(f"{i}. {options}")
    user_answer = input("Enter Your Answer here: ")
    if user_answer in ["1", "2", "3", "4"]:
        selected_option = q["Options"][int(user_answer) - 1]
    else:
        selected_option = user_answer
    if selected_option == q["Answer"]:
        print("Correct!")
        score += 1
    elif selected_option != q["Answer"]:
        print("Incorrect!")
    else:
        print("Enter a valic answer!")
print(f"FINAL SCORE: {score}")
