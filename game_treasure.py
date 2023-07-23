print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure.")
answer1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if answer1 == "left":
  answer2 = input('You are in front of a lake. Do you want to "swim" or "wait" \n').lower()
  if answer2 == "wait":
    answer3 = input('You see flowes. Which color do you pick? "red", "pink" or "purple" \n').lower()
    if answer3 == "red":
      print("The flower has poison. Game over")
    elif answer3 == "purple":
      print("The smell is bad. Game over")
    elif answer3 == "pink":
          print("This flower is the choosen. You win")
    else:
      print("The color doesn't exist. Game over")
  else:
    print("The lake has sharks. Game over")
else:
  print("You can't move. Game over")
