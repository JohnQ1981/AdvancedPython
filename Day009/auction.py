import art
from replit import clear
print(art.text2art("Auc", font='block'))
print(art.text2art("tion", font='block'))
print("Welcome to the secret auction program.")
lp = True
bidders = {}
actual_bidders = []
max_bid = 0
#count = 0
while lp:
    user_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $ "))    
    bidders[user_name] = bid_amount
    #bidders["Bid Amount"] = bid_amount
    #actual_bidders.append(bidders)
    #count += 1
    
    more_bidders = input("Are there any other bidders? Type 'yes' or'no .")
    if more_bidders == 'yes':
        clear()
    elif more_bidders == 'no':
        for bids, values in bidders.items():
            if values > max_bid:
                max_bid = values
        print(f"The winner is: {max_bid} and name is: {bidders.keys()} ")
        lp = False
    else:
        print("incorrect input,try again!")

    print(bidders)
