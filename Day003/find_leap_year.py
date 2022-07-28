print("Welcome to Leap Year Finder")
year = int(input("Enter a year and lets find if it is Leap year or not "))
if year % 4 != 0:
    print(f"Sorry, {year} is not a leap year")
elif year % 100 != 0:
    print(f"Yep, {year} is a leap year")
elif year % 100 == 0:
    if year % 400 == 0:
        print(f" Yep, {year} is a leap year")
    else:
        print(f"Sorry, {year} is not a leap year")

