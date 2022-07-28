print("***Welcome to BMI Calculator***")
height = input("Enter your height in meters: ")
weight = input("Enter Your Weight in kg: ")
bmi = float(weight) / float(height) ** 2
bmi=round(bmi,2)
print(f"{weight} / {height} * {height} = {bmi}")
bmi=round(bmi,2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} which means you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} which means you are normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi} which means you are overweight")
elif bmi >30 and bmi < 35:
    print(f"Your BMI is {bmi} which means you are obese")
else:
    print(f"Your BMI is {bmi} which means you are Clinically Obese")
