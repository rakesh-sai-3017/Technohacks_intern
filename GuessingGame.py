import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"You have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                return True  # Return True if player wins
                
            remaining = max_attempts - attempts
            print(f"Attempts left: {remaining}")
            
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
    
    print(f"\nGame over! The number was {secret_number}.")
    print("Better luck next time!")
    return False  # Return False if player loses

def main():
    while True:
        number_guessing_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
