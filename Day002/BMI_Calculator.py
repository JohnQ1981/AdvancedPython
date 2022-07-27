print("***Welcome to BMI Calculator***")
height = input("Enter your height in meters: ")
weight = input("Enter Your Weight in kg: ")
bmi = float(weight) / float(height) ** 2
bmi=round(bmi,2)
print(f"{weight} / {height} * {height} = {bmi}")
bmi=round(bmi,2)
print(f"Your BMI is {bmi}")
# if you want 