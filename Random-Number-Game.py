# Choose a random number and play with your system and save your hiscore in a file

import random

randNumber = random.randint(1, 100)
# print(randNumber)  # If want to see system random number so uncomment this
guesses = 0
userGuess = None

while (userGuess != randNumber):
    userGuess = int(input("Enter Your guess number: "))
    guesses += 1

    if (userGuess == randNumber):
        print("You guessed a right number !")
    elif (userGuess > randNumber):
        print("You guessed a larger number. Try again !")
    elif (userGuess < randNumber):
        print("You guessed a smaller number. Try again !")
    else:
        ("It's a wrong choice. Please try again !")
print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read())
    if (guesses < hiscore):
        print("You have just broken the hiscore !")
        with open("hiscore.txt", 'w') as f:
            f.write(str(guesses))