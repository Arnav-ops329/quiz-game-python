# This is the main file that contains the overall logic

from questions import questions  # To access the questions from a different file

print("===== WELCOME TO THE QUIZ GAME =====")
input()
print(
    "Some questions would be displayed and you have to answer them, based on the answers you would be granted with points."
)
input()

score= 0 #To set the score of the user to zero
for q in questions:
    print("\n"+ q["Question"])

    for i, options in enumerate(q["Options", start= 1]):
        print(f"{i}. {options}")
        