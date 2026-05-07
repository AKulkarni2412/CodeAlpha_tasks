import random

words = ["apple", "tiger", "chair", "robot", "table"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("You lost! Word was:", word)
