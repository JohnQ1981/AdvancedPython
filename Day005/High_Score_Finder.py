# Instructions
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91
# e.g. When you hit run, this is what should happen:
import art
print(art.text2art("welcome", font='block'), art.text2art("to", font='block'))
print(art.text2art("High Score Finder "))
scores = input("Enter list of Score, and we will find the highest.: ").split()
for c in range(0, len(scores)):
    scores[c] = int(scores[c])
#score_list = list(scores)
#print(score_list)
print(scores)
maxs = 0
for c in scores:
    if c > maxs:
        maxs = c

print(f"Max score is {maxs}")

max_fun = max(scores)
print(max_fun)