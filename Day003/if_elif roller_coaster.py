print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Awesome , you can ride the Rollercoaster")
    age = int(input("Enter your age "))
    ticket = 0
    if age < 12:
        ticket = 5
        print(f"Your ticket will cost ${ticket}.")
    elif age <= 18 and age >= 12:
        ticket = 7
        print(f"Your ticket will cost ${ticket}.")
    else:
        ticket = 12
        print(f"You will be paying full ticket price which is ${ticket}")

    photo = input("Do you want photos? 'Y' or 'N' ")
    if photo == 'Y':
        total = ticket +3
        print(f"Your Total bill is ${total} that is ${ticket} + $3 for photo.")
    else:
        print(f"Your Total bill is ${ticket} ")
else:
    print("Unfortunately you are too short to ride this Rollercoaster")