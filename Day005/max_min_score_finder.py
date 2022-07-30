import art
print(art.text2art("welcome", font='block'), art.text2art("to", font='block'))
print(art.text2art("Min Score Finder "))
while True:
    scores = input("Enter list of Score, and we will find the highest.: ").split()
    for c in range(0, len(scores)):
        scores[c] = int(scores[c])

    min = scores[0]
    max = 0
    for c in scores:
        if c < min:
            min = c
        if c > max:
            max = c
    print(f" Minimum score is : {min} \n and Maximum is : {max}")
    finito = input('Do you want to quit? type "q" to exit ' )
    if finito == 'q':
        print(art.text2art("BYE-BYE", font='block'))
        break