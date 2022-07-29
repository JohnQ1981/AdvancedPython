# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
#print(map)
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
    # count =0
    # for c in map:
    #     if 'X' in c:
    #         count +=1
    #         print(count)
    # if count == 3:
    #     print('*'*45)
    #     row1 = ["⬜️","⬜️","⬜️"]
    #     row2 = ["⬜️","⬜️","⬜️"]
    #     row3 = ["⬜️","⬜️","⬜️"]
    #     map = [row1, row2, row3]
    #     print(f"{row1}\n{row2}\n{row3}")
    # for c in map[2][3]:
    #     for j in map[][]:
    #         if map[c][j] == "X":
    #             print("No Space Left, resetting...")
    #             row1 = ["⬜️","⬜️","⬜️"]
    #             row2 = ["⬜️","⬜️","⬜️"]
    #             row3 = ["⬜️","⬜️","⬜️"]
    #             map = [row1, row2, row3]
    #             print(f"{row1}\n{row2}\n{row3}")



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")
    reset_or_not = input("Do you want to reset? Type 'Y' or 'N' or 'Q' to quit ").lower()
    if reset_or_not == 'y':
        print('*'*45)
        row1 = ["⬜️","⬜️","⬜️"]
        row2 = ["⬜️","⬜️","⬜️"]
        row3 = ["⬜️","⬜️","⬜️"]
        map = [row1, row2, row3]
        print(f"{row1}\n{row2}\n{row3}")
    elif reset_or_not == 'q':
        break