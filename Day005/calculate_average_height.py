# Instructions
# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
import art
print('''  \_/
  --(_)--  .
    / \   /_\
          |Q|
    .-----' '-----.                                  __
   /____[SCHOOL]___\                                ()))
    | [] .-.-. [] |                                (((())
  ..|____|_|_|____|..................................)(... 
''')
print(art.text2art("Hello", font='block'))
print("Welcome to Average Height Calculator ")
list_of_heights = input("Enter List of Heights of students ")
students = list_of_heights.split(" ")
print(students)
sum = 0
for c in students:
    sum += int(c)
average = round(sum/len(students))
print(f"Total sum is :{sum} and Average is {average}")

