import random
from random import randint
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
while True:
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
    ran = randint(0,len(names)-1)
    print(f"{names[ran]} is going to buy the meal today!")