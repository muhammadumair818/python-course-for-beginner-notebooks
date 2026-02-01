"""
NUMBER GUESSING GAME

A simple game where the computer picks a random number
and the player tries to guess it.

Features:
- Random number generation
- User input validation
- Feedback (too high, too low, correct)
- Track number of attempts
- Play again option
"""

import random

def play_game():
    """Play a single round of the guessing game"""
    
    # Computer picks a random number between 1 and 100
    target = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("\n" + "="*50)
    print("WELCOME TO NUMBER GUESSING GAME!")
    print("="*50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("-"*50)
    
    while not guessed:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            
            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            attempts += 1
            
            # Check the guess
            if guess == target:
                guessed = True
                print(f"\n🎉 Correct! The number was {target}")
                print(f"You took {attempts} attempts!")
                
                # Rate the performance
                if attempts <= 3:
                    print("🌟 Amazing! You're a genius!")
                elif attempts <= 7:
                    print("👍 Great job!")
                else:
                    print("💪 Nice try! Keep practicing!")
            
            elif guess < target:
                print(f"Too LOW! Try a higher number. (Attempt {attempts})")
            
            else:
                print(f"Too HIGH! Try a lower number. (Attempt {attempts})")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main game loop"""
    
    play_again = True
    
    while play_again:
        play_game()
        
        # Ask if user wants to play again
        response = input("\n\nDo you want to play again? (yes/no): ").lower()
        
        if response not in ['yes', 'y']:
            play_again = False
            print("\nThanks for playing! Goodbye! 👋")
    
    print("="*50)

if __name__ == "__main__":
    main()
