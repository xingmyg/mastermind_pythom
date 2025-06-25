# MasterMiimport random
# by ICTROCN
# v1.01qw		qq12
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random

VALID_COLORS = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

def generate_code():
    return [random.choice(colors) for _ in range(4)]

def get_feedback(secret, guess):
    guess = [color.lower() for color in guess]

    black_pegs = sum(s == g for s, g in zip(secret, guess))
    secret_counts = {}
    guess_counts = {}

def is_admin():
    password = input("Enter admin password: ")
    return password == "letmein123"

def show_secret(code):
    print("Admin-only: The secret code is:", ' '.join(code))

    # Count whites by subtracting black and calculating min digit frequency match
    secret_Code = generate_Code()
    attempts = 10

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(color, 0), guess_counts.get(color, 0)) for color in guess_counts)
    return black_pegs, white_pegs

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4 color code, Choose from:", ', '.join(VALID_COLORS))
    print("You have 10 attempts.\n")

    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_guess = False
        while not valid_guess:
            guess_input = input(f"Attempt {attempt}: ").strip().lower()

            if guess_input == "cheat":
                if is_admin():
                    show_secret(secret_code)
                else:
                    print("Access denied.")
                continue

            guess_list = guess_input.split()
            valid_guess = len(guess_list) == 4 and all(color in VALID_COLORS for color in guess_list)

        if not valid_Guess:
           print("Invalid input. Please enter 4 valid colors separated by spaces.")

        black, white = get_feedback(secret_code, guess_list)
        print(f"Black pegs (correct color & position): {black}")
        print(f"White pegs (correct color, wrong position): {white}\n")

        if black == 4:
    print(f"Congratulations! You guessed the code: {' '.join(secret_code)}")
    return

print(f"Game over! The correct code was: {' '.join(secret_code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

