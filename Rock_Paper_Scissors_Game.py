print("Rock Paper Scissors Game")
choise = input("what do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")

rock = ('''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
''')

paper = ('''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
''')

scissors = ('''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
''')

itens = [rock, paper, scissors]
if choise == "0":
    print(rock)
elif choise == "1":
    print(paper)
else:
    print(scissors)

computer = len(itens)
computer_pick = random.randint(0, computer -1)
computer_choice = itens[computer_pick]
print(f"computer choice:\n {computer_choice}") 

if choise == "0" and computer_pick == 2:
    print("You won")
elif choise == "2" and computer_pick == 1:
    print("You won")
elif choise == "1" and computer_pick == 0:
    print(" You won")
else:
    print("You lose")  

