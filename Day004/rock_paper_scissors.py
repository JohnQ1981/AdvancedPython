from random import randint
import art
print("""                                   __,...__
                               _,-'::::::::`-.
                             ,'::,----._::::::`.
                           ,'::,' /\,-. \:::::::`.
                          /::::| ;    | |:::::::::`.
                          |:::::`._   \ |:::::::::::\\
                        __\,:--''--`_--':::::::::::::\\
                      `'--::__:::::::`-:_:::::::::::::\\
                          /--.`'--:_:::::`-::::::::::::\\
                         /,-_.'    _`-:_::::`:::::::::::\\
                         / /o\|   ,-_`-.`--:::`::::::::::)
                        || \_/|  / /o\\         `:,'''-:'
                      (#__`-_/   | \_/|        /##|  ,-.\\
                     ,''     `-. `.__/       ,'###| /   ||
                    /           \      ,    (##### /    ||
                    |           |___,-##\     /##/ \__,'/
                    \          /########)    |#,'|__..-'
                     `-..__..-'######)          /
                         \`.###'`""'           /
                          \\\__//            ,'
                           \`--'         _,-'
                            `-..___..--''
""")
print(art.text2art("WELCOME", font='block'))
while True:
    ran = randint(1,3)
    computer = ""
    #print(ran)
    rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if ran == 1:
        computer = rock
        #print(rock)
    elif ran == 2:
        computer = paper
        #print(paper)
    elif ran == 3:
        computer = scissors
        #print(scissors)
    
    user = input("Enter your choice as 'rock, 'paper' or 'scissors' \n").lower()
    if user == 'rock':
            user = rock
            print(rock)
    elif user == 'paper':
            user = paper
            print(paper)
    elif user == 'scissors':
            user = scissors
            print(scissors)
    else:
        print("Try again")

    if (user == rock and computer == rock ) or  (user == paper and computer == paper ) or (user == scissors and computer == scissors ):
            print('It is Tie')     
    elif (user == rock and computer == scissors ) or  (user == paper and computer == rock ) or (user == scissors and computer == paper ):
            print("You won!")
            print(user, computer)
            break
    elif user != rock and user != paper and user != scissors:
        print("Not correct value entered")    
    else:
            print("You lost, Try again")

    print(user, computer)
