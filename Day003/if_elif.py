print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Awesome , you can ride the Rollercoaster")
    age = int(input("Enter your age "))
    if age < 12:
        print("Your ticket will cost $5.")
    elif age <= 18 and age >= 12:
        print("Your ticket will cost $7.")
    else:
        print("You will be paying full ticket price which is $15")
else:
    print("Unfortunately you are too short to ride this Rollercoaster")