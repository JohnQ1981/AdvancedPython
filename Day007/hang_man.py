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
guess_word = input("Enter Letter of the Word Generated")