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
print(ran)
kelime =''
blank_list = []
display = []
for c in ran:
  blank_list.append("_")
  display += "_"
print(blank_list, len(blank_list), display)
for c in ran:
  kelime += "_"
print(kelime, len(kelime))
countb = 0
while countb < len(ran):
  guess_word = input("Enter Letter of the Word Generated1 ")
  countb += 1
  if guess_word in ran: 
    print(f"{kelime} su ana kadar {ran[ran.find(guess_word)]} and index is {ran.find(guess_word)}")
    kelime = kelime[:ran.find(guess_word)] + guess_word + kelime[ran.find(guess_word)+1:]
  for c in ran:
    if guess_word in ran:
      blank_list.insert(ran.find(guess_word),guess_word)
      blank_list.pop(ran.find(guess_word)+1)
  print(blank_list, len(blank_list))
  print(f"{kelime}")
  
  for position in range(len(ran)):
    letter = ran[position]
    if letter == guess_word:
      display[position] = letter
  print(display)  
  for c in ran:
    if c == guess_word:
      print("Right")
    else:
      print("Wrong")
  guess = list(ran)
  print(guess)
  print(f"Count is :{countb}")
  if kelime == ran or display == guess:
    print("You Won")
    break
  elif display != guess and countb == len(ran):
    print("You lost")