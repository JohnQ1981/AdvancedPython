# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
actual_days = 90 * 365
actual_weeks = 90 * 52
actual_months = 90 *12
# print(actual_days)
# print(actual_weeks)
# print(actual_months)
days_left = actual_days - (age * 365)
weeks_left = actual_weeks - (age * 52)
months_left = actual_months - (age *12)
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
# other solution
years_left = 90 - age
days_remaining = years_left * 365
weeks_remaining = years_left * 52
months_remaining = years_left *12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")