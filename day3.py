import random

def number_guessing_game():
    number_to_guess = random.randint(1, 50)
    max_tries = 7
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 50. You have 7 tries to guess it.")

    while attempts < max_tries:
        user_input = input(f"\nAttempt {attempts + 1}/{max_tries} - Enter your guess: ")
        
        # Check if input is a valid integer (handling letters/edge cases)
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid number between 1 and 50.")
            continue
            
        guess = int(user_input)
        attempts += 1
        if guess < 1 or guess > 50:
            print("Please keep your guess between 1 and 50.")
            continue

        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} tries!")
            break
    else:
        print(f"\nGame Over! The correct number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()