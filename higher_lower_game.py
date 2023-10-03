#my code
#print logo
from game_data import data
import random
#from replit import clear
from game_data import logo
#print random name vs other
# creat function that takes one name of the dictionary, explains job and country.
print(logo)
name1 = random.sample(data, 1)
def ny (name1):
  return(f'Compare A: {name1[0]["name"]}, a {name1[0]["description"]}, from {name1[0]["country"]}')
print(ny(name1))
print("\nVS\n")

name2 = random.sample(data, 1)
def na(name2):
  return(f'Compare B: {name2[0]["name"]}, a {name2[0]["description"]}, from {name2[0]["country"]}') 
print(na(name2))

# #creat a function to compare de highest value between them. 
def comp(name1, name2):
  if name1[0]["follower_count"] > name2[0]["follower_count"]:
      return "a"
  else:
    return "b" 
#print(comp(name1, name2))

# ask what is the highest value. 
comparison = input("Who has more followers? Type 'A' or 'B': ").lower()
end_of_game = False
# if answer is right compare the last value with another random
score = 0
while not end_of_game:
  if comp(name1, name2) == comparison:
    score += 1
    #clear()
    #print(logo)
    print(f"You're right! Current score: {score}.")
    print(ny(name2))
    name2 = random.sample(data, 1)
    print("VS")
    print(na(name2))
    #print(comp(name1, name2))
    comparison = input("Who has more followers? Type 'A' or 'B': ").lower()
    
  else:
    print("Sorry, you got it wrong")
    end_of_game = True

# print you are righ and current score
# show how many times the player answered right
# if the palyer answer wrong print the hits and finish the game
print(f"Final score: {score}.")
