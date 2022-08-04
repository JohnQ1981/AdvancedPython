#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for c in range (2 ,number):
        if number % c == 0:
            is_prime = False
    if is_prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
        






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