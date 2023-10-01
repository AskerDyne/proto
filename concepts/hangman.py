# Imports
import random

# Configuration
word_list = ["ardvark", "camel", "hamster", "baboon"]
hang_word = random.choice(word_list)
hang_word_len = len(hang_word)
hang_list = ["_"] * hang_word_len

print("\n(for display purposes)\nThe word is:", hang_word, "\n")
print(" ".join(hang_list))

# Simple hangman game
while True:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("(please enter a single letter)")
        continue

    if guess in hang_word:
        for i in range(hang_word_len):
            if hang_word[i] == guess:
                hang_list[i] = guess
        print("\nCorrect:", guess)
    else:
        print("\nWrong")

    print(" ".join(hang_list))

    if "_" not in hang_list:
        print("\nCongratulations!\nYou've guessed the word:", hang_word)
        break