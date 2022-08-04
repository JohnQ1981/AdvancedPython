import random
import art
print('''_____
        |   D
        |   |
        |   |
        \___|            _
          ||  _______  -( (-
          |_'(-------)  '-'
             |       /
      _____,-\__..__|_____Pr59''')
print(art.text2art("Hello", font='block'))
print(art.text2art("Wlcm", font ='block'))
words = ['alican', 'velicana', 'delicana', 'talican', 'hilola','abdurrahmon']
ran = random.choice(words)
print(ran, len(ran))
display = []
for c in ran:  
  display += "_"
print(display)
countb = 0
while countb < len(ran):
  guess_word = input("Enter Letter of the Word Generated1 ")
  countb += 1
  for position in range(len(ran)):
    letter = ran[position]
    if letter == guess_word:
      display[position] = letter
  print(display)
  print(f"Count is :{countb}")
  guess = list(ran)
  if display == guess:
    print("You Won")
    break
  elif display != guess and countb == len(ran):
    print("You lost")  