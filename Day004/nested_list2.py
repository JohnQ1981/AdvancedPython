# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
while True:
    position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
    row = position[0]
    column = position[1]
    print(row,column)
    column = int(column)
    row = int(row)
    map[column-1][row-1] = 'X'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")
    print('*'*45)
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")