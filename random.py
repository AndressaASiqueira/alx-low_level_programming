import random
test_seed = int(input("Creat a seed number: "))
random.seed(test_seed)
coin = random.randint(0,1)
if coin == 0:
  print("Heads")
else:
  print("Tails")
