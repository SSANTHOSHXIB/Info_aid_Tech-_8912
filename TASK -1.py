import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number ({number_to_guess}) correctly in {attempts} attempts!")
            return True

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}. Game over!")
    return False

def main():
    welcome()
    while True:
        if play_game():
            play_again = input("Do you want to play again? (Yes/No): ")
            if play_again.lower() != 'yes':
                print("Thank you for playing!")
                break
            else:
                print("\nLet's play again!")
                continue
        elif not play_game():
            play_again = input("Do you want to play again? (Yes/No): ")
            if play_again.lower() != 'yes':
                print("Thank you for playing!")
                break
            else:
                print("\nLet's play again!")
                continue

if __name__ == "__main__":
    main()
