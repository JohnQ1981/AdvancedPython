print("Welcome to the tip Calculator. \n")
bill_paid = float(input("What was the total bill paid? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
how_many_people = int(input("How many people to split the bill? "))
each_pays = ((bill_paid * tip_percentage / 100) + (bill_paid)) / how_many_people
total = ((bill_paid * tip_percentage / 100) + (bill_paid))
tip_percentage = (bill_paid * tip_percentage / 100)
print(f"Total will including the tip percentage is: {round(total,2)}, and Tip paid {round(tip_percentage,2)}")
print(f"Each Person should pay: ${round(each_pays,2)}")

