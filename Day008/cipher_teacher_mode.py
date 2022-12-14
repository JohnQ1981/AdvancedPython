#import artt
import art
import math
print(art.text2art("CAESAR", font='block'))
print(art.text2art("cipher", font='block'))
#print(artt.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if shift > len(alphabet):
    #     shift = math.floor(shift % 52/2)
    #print(len(alphabet), shift)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")
    def all_in_one(plain_text, shift_amount, direction):
        if direction == 'encode':
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"The encoded text is {cipher_text}")
        elif direction == 'decode':
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                cipher_text += alphabet[new_position]
            print(f"The decoded text is {cipher_text}")
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ''
        if shift_amount > len(alphabet)/2:
            shift_amount = math.floor(shift % 52/2)
        if cipher_direction == 'decode':
                shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else :
                end_text += letter
        print(f"The {cipher_direction}d text is {end_text}")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##????Bug alert: What happens if you try to encode the word 'civilization'?????

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    #all_in_one(plain_text = text, shift_amount = shift, direction = direction)
    caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
    # if direction == 'encode':
    #     encrypt(plain_text=text, shift_amount= shift)
    # elif direction == 'decode':
    #     decrypt(cipher_text=text, shift_amount= shift)
    # else:        
    end_it = input("Enter 'q' to end or blank to continue ")
    if end_it == 'q' or end_it == 'Q':
        print(art.text2art("bye", font='block'))
        break
    else:
        continue