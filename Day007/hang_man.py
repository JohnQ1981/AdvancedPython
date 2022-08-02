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
words = ['Alican', 'Velican', 'Delican', 'Talican']
ran = random.choice(words)
print(ran)
kelime = []
hesap = 0
guess_word = input("Enter Letter of the Word Generated ")
for c in ran:
  if guess_word == ran:
    kelime.append(guess_word)
    print(f"{kelime} su ana kadar")
  if kelime == ran:
    print("You Won")
  else:
    guess_word = input("Enter Letter of the Word Generated ")
  if guess_word != ran:
    hesap += 1
    if hesap == len(ran):
      print("Game Over")
    elif hesap < len(ran):
      guess_word = input("Enter Letter of the Word Generated")
    else:
      print('You Won!')

