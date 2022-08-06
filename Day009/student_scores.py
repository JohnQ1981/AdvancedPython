import art
print(art.text2art("dict", font='block'), art.text2art("ion", font='block'),art.text2art("ary", font='block'))
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# for k in student_scores:
#   if student_scores[k] <= 70:
#     student_grades[k] = 'Fail'
#     student_scores[k] = 'Fail'
#   elif student_scores[k] >= 71 and student_scores[k] <= 80:
#     student_grades[k] = 'Acceptable'
#     student_scores[k] = 'Acceptable'
#   elif student_scores[k] >= 81 and student_scores[k] <= 90:
#     student_grades[k] = 'Exceeds Expectations'
#     student_scores[k] = 'Exceeds Expectations'
#   elif student_scores[k] >= 91 and student_scores[k] <= 100:
#     student_grades[k] = 'Outstanding'
#     student_scores[k] = 'Outstanding'

#other solution
for k in student_scores:
  score = student_scores[k]
  if score > 90:
    student_grades[k] = "Outstanding"
  elif score > 80 :
    student_grades[k] = "Exceeds Expectations"
  elif score > 70:
    student_grades[k] = "Acceptable"
  else:
    student_grades[k] = "Fail"

    

# 🚨 Don't change the code below 👇
print(student_grades)
print("*"*50)
print(student_scores)





