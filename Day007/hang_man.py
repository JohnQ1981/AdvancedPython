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
words = ['Alican', 'Velican', 'Delican', 'Talican', 'Hilola','Abdurrahmon']
ran = random.choice(words)
print(ran)
kelime =''
#kelime = ran.replace("", "*")
for c in ran:
  kelime += "_"
print(kelime, len(kelime))
# word_blank = str(len(kelime))
# print(word_blank)
# print(kelime)
# hesap = 0
while True:
  guess_word = input("Enter Letter of the Word Generated1 ")
  if guess_word in ran: 
    print(f"{kelime} su ana kadar {ran[ran.find(guess_word)]} and index is {ran.find(guess_word)}")
    kelime = kelime[:ran.find(guess_word)] + guess_word + kelime[ran.find(guess_word)+1:]
    #kelime[int(ran.find(guess_word))] = guess_word
    #kelime = kelime.replace(int(ran.find(guess_word)),ran[ran.find(guess_word)])
  print(f"{kelime}")
  if kelime == ran:
    break
  # if kelime == ran:
  #   print("You Won")
  # else:
  #   guess_word = input("Enter Letter of the Word Generated2 ")
  # if guess_word != ran:
  #   hesap += 1
  # if hesap == len(ran):
  #     print("Game Over")
  # elif hesap < len(ran):
  #     guess_word = input("Enter Letter of the Word Generated3")
  # else:
  #     print('You Won!')

