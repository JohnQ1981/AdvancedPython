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
words = ['alican', 'velica', 'delica', 'talica', 'hilola','salih']
ran = random.choice(words)
print(ran, len(ran))
display = []
for c in ran:  
  display += "_"
print(display)
countb = 0
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_game = False
lives = 6
while not end_game:
  guess_word = input("Enter Letter of the Word Generated1 ")
  countb += 1
  
  for position in range(len(ran)):
    letter = ran[position]
    if letter == guess_word:
      display[position] = letter
    

  if guess_word not in ran:
      lives -=1
      print(f"{stages[lives]}")
      if lives == 0 :
        end_game = True
        print("You Lost")

  print(display)
  print(f"Count is :{countb}, be careful and you have only {len(ran)-countb+1} guess(s) left. ")
  guess = list(ran)
  if display == guess or "_" not in display:
    print("You Won")
    break
  elif display != guess and lives == 0:
    print("You lost")
    break

          
