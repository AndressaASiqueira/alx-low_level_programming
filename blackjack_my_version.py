############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random 
from art import logo
import collections  
#import clear 

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

 #start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
 start = input("Vc quer jogar 21/Blackjack? Type 'y' or 'n': ")
 if start == "y":

  def deal_card(round):
      card = []
      card = random.choice(cards)
      return card
  
  user_cards = []
  for i in range(2):
     i = deal_card(2)
     user_cards.append(i) 
  print(f"Your cards: {user_cards}")
  
  computer_cards = []
  for i in range(2):
     i = deal_card(5)
     computer_cards.append(i) 
  
  def calculate_score(list_cards):
    blackjack = [10, 11] 
    if collections.Counter(user_cards)  == collections.Counter(blackjack) or collections.Counter(computer_cards) == collections.Counter(blackjack):
      return 0
    elif sum(list_cards) > 21:
      return sum(list_cards)
      if sum(list_cards) == [11]:
        list_cards.remove(11)
        list_cards.append(1)
        return sum(list_cards)
    else:
      return sum(list_cards)
  print(f"Your score: {calculate_score(user_cards)}")
  
  print(f"Computer cards: {computer_cards[0]}")

  end_of_game = True
   
  if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0:
      print("Blackjack, End of game")
      end_of_game = False
      blackjack()
    
  elif calculate_score(user_cards) > 21:
      print(f"Your final score: {calculate_score(user_cards)}")
      end_of_game = False
      blackjack()
  
  while end_of_game: 
    
    #another_round = input("Type 'y' to get another card, type 'n' to pass: ")
    another_round = input("Digite 'y' para obter outra carta, digite 'n' para passar: ")
  
    if another_round == "y":
      user_cards.append(deal_card(1))
      print(f"Your cards: {user_cards}")
      print(f"Your score: {calculate_score(user_cards)}")
      if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0:
        print("End of game")
        end_of_game = False
      elif calculate_score(user_cards) >= 21:
        print(f"Your final cards: {user_cards}")
        print(f"Your final score: {calculate_score(user_cards)}")
        print("End of game")
        end_of_game = False
    
    elif another_round == "n":
      
      while calculate_score(computer_cards) <= 17:
        computer_cards.append(deal_card(1))
      if calculate_score(computer_cards) > 17:
          print(f"Computer cards: {computer_cards}")
          print(f"Computer final score:{calculate_score(computer_cards)}")
          print("End of game")
          end_of_game = False
      elif calculate_score(computer_cards) > 21: 
        print("End of game")
        end_of_game = False
      else:
         print(f"Computer cards: {computer_cards}")
         print(f"Computer final score:{calculate_score(computer_cards)}")
        
  def compare():
    if calculate_score(user_cards) > 21:
      print("You lose")
      blackjack()
    elif calculate_score(computer_cards) > 21:
      print("You win")
      blackjack()
    elif calculate_score(user_cards) > calculate_score(computer_cards):
      print("You win")
      blackjack()
    elif  calculate_score(computer_cards) > calculate_score(user_cards):
      print("You lose")
      blackjack()
    elif calculate_score(computer_cards) == calculate_score(user_cards):
      print("Its a Draw")
      blackjack()
    elif calculate_score(user_cards) == 0:
      print("BlackJack \n You win")
      blackjack()
    elif calculate_score(computer_cards) == 0:
      print("BlackJack \n You lose")
      blackjack()
    else:
      print("You lose 😤")
      blackjack()
  compare()

#clear()  
blackjack()  
    
    
    
    

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

