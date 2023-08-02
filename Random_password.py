import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#My own code 

letters1 = 0
for x in range(nr_letters):
   letters1 = random.sample(letters, nr_letters)

numbers1 = 0
mumbers1 = []
for i in range(nr_numbers):
    numbers1 = random.sample(numbers, nr_numbers)

symbols1 = 0
symbols1 = []
for i in range(nr_symbols):
    symbols1.append(random.choice(symbols)) 

password = (letters1)+(numbers1)+(symbols1)
random.shuffle(password)
password = ''.join(password)
print(f" Here is your password: {password}")

#Teacher explanation               
# Eazy level: Add the random values in same string 
password1 = ""
for char in range(1, nr_letters +1):
    password1 += random.choice(letters)

for char in range(1, nr_symbols +1):
    password1 += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password1 += random.choice(numbers)

print(password1)     

# Hard level: Creat a list to make the values shuffled. 

password_list = []

for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols +1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
