import random

def roll_dice(num_dice):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the Dice Roller!")
    while True:
        num_dice = int(input("How many dice would you like to roll? "))
        if num_dice <= 0:
            print("Please enter a valid number of dice.")
            continue
        
        rolls = roll_dice(num_dice)
        print("Result:", rolls)
        
        roll_again = input("Would you like to roll again? (yes/no) ").strip().lower()
        if roll_again != 'yes':
            print("Thank you for using the Dice Rolling App!")
            break

if __name__ == "__main__":
    main()
