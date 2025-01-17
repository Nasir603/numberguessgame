from pickle import GLOBAL
import random
from art import logo
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

guess_n = random.choice(numbers)
attempts = 0
def num_guess_game():
    global attempts
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    e_h = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if e_h == "easy":
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    def guess_again():
        global attempts
        u_guess = int(input("Make a guess: "))
        if u_guess == guess_n:
            print(f"You got it! The answer was {u_guess}")
        else:
            if u_guess < guess_n:
                print("Too Low.\nGuess again.")
                attempts -= 1
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif u_guess > guess_n:
                print("Too high.\nGuess again.")
                attempts -= 1
                print(f"You have {attempts} attempts remaining to guess the number.")
    should_continue = True
    while should_continue:
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            should_continue = False
        else:
            guess_again()
num_guess_game()
