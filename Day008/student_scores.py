student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {'Harry' : 'Exceeds Expectations'}
val = []
#TODO-2: Write your code below to add the grades to student_grades.👇
for keys, values in student_scores.items():
    # if student_scores.values <= 70:
    #     student_grades.update(val)
    print(f"{keys} --- {values}")
    val.append(values)
for c in val:
    if c <= 70:
        
print(val)
# 🚨 Don't change the code below 👇
print(student_grades)