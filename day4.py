def get_guess():
    """Prompts the user to enter their guess and returns it as an integer."""
    return int(input("Enter your guess: "))

def check_guess(guess, secret_number):
    """Compares the user's guess with the secret number and returns the result."""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"

def play_round():
    """Manages a single round of the guessing game using helper functions."""
    # Chote functions ko test karna isliye aasan hota hai kyunki 
    # aap har function (jaise check_guess ya get_guess) ko alag se 
    # bina poora game run kiye verify kar sakte hain.
    secret_number = 7
    while True:
        guess = get_guess()
        result = check_guess(guess, secret_number)
        if result == "correct":
            print("You guessed it right!")
            break
        elif result == "low":
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_round()