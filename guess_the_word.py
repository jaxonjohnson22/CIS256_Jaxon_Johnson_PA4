
# Jaxon Johnson
# CIS256 Fall 2026
# Programming Assignment 4

import random

# These are the words the game can choose from.
WORDS = ["python", "computer", "student", "keyboard", "program"]


def choose_word(words=WORDS):
    """Choose and return a random word from the word list."""
    if not words:
        raise ValueError("The word list cannot be empty.")

    return random.choice(words)


def display_word(word, guessed_letters):
    """Show guessed letters and hide letters not guessed yet."""
    displayed = []

    for letter in word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append("_")

    return " ".join(displayed)


def check_guess(word, guess):
    """Return True when the guessed letter is in the word."""
    return guess.lower() in word.lower()



def play_game():
    """Run the word guessing game and allow replaying."""
    play_again = "yes"

    while play_again == "yes":
        word = choose_word()
        guessed_letters = set()
        incorrect_guesses = set()
        attempts_left = 6

        print("\nWelcome to the Word Guessing Game!")
        print("Guess the word one letter at a time.")
        print("You have 6 incorrect guesses available.")

        while attempts_left > 0:
            print("\nWord:", display_word(word, guessed_letters))
            print("Incorrect guesses:", ", ".join(sorted(incorrect_guesses)))
            print("Attempts left:", attempts_left)

            guess = input("Enter a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter one letter at a time.")
                continue

            if guess in guessed_letters or guess in incorrect_guesses:
                print("You already guessed that letter. Try another one.")
                continue

            if check_guess(word, guess):
                guessed_letters.add(guess)
                print("That is correct!")

                if all(letter in guessed_letters for letter in word):
                    print("\nCongratulations! You guessed the word:", word)
                    break
            else:
                incorrect_guesses.add(guess)
                attempts_left -= 1
                print("That letter is not in the word.")

        if attempts_left == 0:
            print("\nYou ran out of attempts. The word was:", word)

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        while play_again not in ("yes", "no"):
            play_again = input("Please enter yes or no: ").strip().lower()

    print("Thanks for playing!")

