from replit import clear
from logos import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    try: 
        return n1 / n2
    except ZeroDivisionError:
        return "Cannot divide by zero!"
def calculator():
  print(logo)

operations = {"+": add, 
        "-": subtract, 
        "*": multiply, 
        "/":divide
       }
while True:
    num1 = int(input("What is the first number?"))
    for k in operations:
        print(k)
    operator = input("what operation you want to perform? : pick from above ")
    num2 = int(input("What is the next number?"))
    calculation_function = operations[operator]
    #print(operations[operator])
    first_answer = calculation_function(num1, num2)



    print(f"{num1} {operator} {num2} = {first_answer}")
    operator = input("pick another operation:")
    num3 = int(input("What is the next number?"))
    calculation_function = operations[operator]
    second_answer = calculation_function(first_answer, num3)
    print(f"{first_answer} {operator} {num3} = {second_answer}")
    end_it = input("Enter 'q' to end ")
    if end_it == 'q' or end_it == 'Q':
        break
    else:
        clear()
        calculator()
        continue
calculator()
# if operator == "+":
#     print(f"{num1} {operator} {num2} = {add(num1,num2)}")
# elif operator == "-":
#     print(f"{num1} {operator} {num2} = {subtract(num1,num2)}")
# elif operator == "*":
#     print(f"{num1} {operator} {num2} = {multiply(num1,num2)}")
# elif operator == "/":
#     print(f"{num1} {operator} {num2} = {divide(num1,num2)}")
# else:
#     print("Incorrect operation")
# for c in operations.keys():
#     if c == operator:

#         print(operations[c])