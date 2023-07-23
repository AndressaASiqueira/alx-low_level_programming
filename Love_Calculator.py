print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
low_case = combined_string.lower()

t = low_case.count("t") 
r = low_case.count("r") 
u = low_case.count("u") 
e = low_case.count("e")

true = t + r + u + e

l = low_case.count("l") 
o = low_case.count("o") 
v = low_case.count("v") 
e = low_case.count("e") 

love = l + o + v + e

true_love = int(str(true) + str(love))


if int(true_love) < 10 or int(true_love) > 90:
  print(f'Your score is {true_love}, you go together like coke and mentos.')
elif true_love >= 40 and true_love <= 50:
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")
