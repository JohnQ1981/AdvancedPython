#Write your code below this line 👇
def prime_checker(number):
    if n == 2:
        print("It's a prime number.")
    elif n == 3:
        print("It's a prime number.")
    elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")






#Write your code above this line 👆
    
#Do NOT change any of the code below👇
while True:
    n = int(input("Check this number: "))
    prime_checker(number=n)
    end_it = input("Enter 'q' to end ")
    if end_it == 'q' or end_it == 'Q':
        break
    else:
        continue