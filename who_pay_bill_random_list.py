#Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
size_names = len(names)
random_name = random.randint(0, size_names -1)
final_name = names[random_name]
print(f"{final_name} is the one who gonna pay the bill today")
