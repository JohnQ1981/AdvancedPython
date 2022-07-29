import random
import art
print('''_____
        |   D
        |   |
        |   |
        \___|            _
          ||  _______  -( (-
          |_'(-------)  '-'
             |       /
      _____,-\__..__|_____Pr59''')
print(art.text2art("Hello", font='block'))
print("Welcome to Password Generator ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#password_length = input("What length do you want your password to be? \n")
while True:
    user_letter = input("How many letter do you want in your password? \n")
    user_numbers = input("How many numbers do you want to be in your password? \n")
    user_symbol = input("How many symbols do you want in your password? \n")
    password = []
    for c in range(0,int(user_letter)):
        password.append(random.choice(letters))
    for j in range(0,int(user_numbers)):
        password.append(random.choice(numbers))
    for k in range(0,int(user_symbol)):
        password.append(random.choice(symbols))

    print(password)
    print("*"*100)
    for l in password:
        random.shuffle(password)
        print(password)
    print("*"*100)
    print(f"Your Password is {password}")
    end_or_no = input(" Do you want to generate more or quit? Type 'Y' to continue and 'q' to quit ")
    if end_or_no == 'q' or end_or_no == 'Q':
        break
    


