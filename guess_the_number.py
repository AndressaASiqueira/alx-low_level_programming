#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random 

#My code

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

mood = input("Choose a difficulty. Type 'easy' or 'hard': ")

# random number
number = random.randint(1, 100)
print(number)

def type(): 
  """Mode of the game"""
  if mood == "easy":
    return 11
  else:
    return 6

attempts = type()

def score():
  """Function to calculate if the game is end or not"""
  global attempts
  if attempts == 1 and choose_number < number:
    return "Too low.\nYou've run out of guesses, you lose."
  elif attempts == 1 and choose_number > number:
    return "Too high.\nYou've run out of guesses, you lose."
  elif choose_number > number:
    return "Too high.\nGuess again."
  elif choose_number < number:
    return "Too low.\nGuess again."
  elif choose_number == number:
    return f"You got it! The answer was {number}."

#Loop to run until the attempts are finished or the answer is right
while attempts > 0: 
  
  attempts -= 1

  if attempts > 0:
   print(f"You have {attempts} attempts remaining to guess the number")
   choose_number = int(input("Make a guess: "))
   print(score())
   if choose_number == number:
     attempts = 0
