import art
from replit import clear
import random
print(art.text2art("BLKJCK", font='block'))
cards = [2,3,4,5,6,7,8,9,10]
dealer = []
computer = []
if input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")== 'y':
    for c in range(0,2):
        dealer.append(random.choice(cards))
        sum = 0
        for k in dealer:
            #print(k)        
            sum += k
    for c in range(0,1):
        computer.append(random.choice(cards))
        csum = 0
        for k in computer:
            csum +=k    
    print(f"Your cards: {dealer}, current score: {sum}")
    print(f"Computer's first card :{csum}")
    extra_card = input("Type 'y' to get another card, type 'n' to pass:")
    if extra_card == 'y':
        for c in range(0,1):
            dealer.append(random.choice(cards))
            sum = 0
            for k in dealer:
                #print(k)        
                sum += k
    print(f"Your cards: {dealer}, current score: {sum}")
    print(f"Computer's first card :{csum}")
    extra_card = input("Type 'y' to get another card, type 'n' to pass:")

