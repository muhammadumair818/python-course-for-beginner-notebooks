# Number Guessing Game

A fun interactive game where you guess a random number!

## Features

- Random number between 1-100
- Feedback on each guess (too high/low)
- Attempt counter
- Performance rating
- Play multiple rounds

## How to Play

```bash
python game.py
```

1. The computer picks a random number
2. You guess the number
3. Get feedback if your guess is too high or too low
4. Keep guessing until you find the number
5. Play again if you want!

## Sample Output

```
==================================================
WELCOME TO NUMBER GUESSING GAME!
==================================================
I'm thinking of a number between 1 and 100.
Can you guess it?
--------------------------------------------------
Enter your guess: 50
Too HIGH! Try a lower number. (Attempt 1)

Enter your guess: 25
Too LOW! Try a higher number. (Attempt 2)

Enter your guess: 37
🎉 Correct! The number was 37
You took 3 attempts!
🌟 Amazing! You're a genius!
```

## Learning Concepts

- `random.randint()` for random numbers
- `while` loops for game logic
- `if/elif/else` for decision making
- User input validation
- Try-except for error handling
- Function organization

---

Have fun playing! 🎮
