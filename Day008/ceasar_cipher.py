import art
print(art.text2art("Hello", font='block'))
def encrypt():
    a = input("Enter the Text to encrypt ").lower()
    b = int(input("Enter Shift "))
    print(f"You entered {a} and {b}")
    for c in a:
        print(f"ASCII Value of {c} is {ord(c)} ")
    for c in a:
        print(f"Encrypted ASCII Value of {c} is {ord(c)+b} ")
    d= ''
    for c in a:
        d += chr(ord(c)+b) 
        print(f"Here is the encrypted version {chr(ord(c)+b)}")
    print(d)
def decrypt():
    k = input("Enter the Text to decrypt ").lower()
    l = int(input("Enter Shift number to decrypt "))
    print(f"You entered {k} and {l}")
    for c in k:
        print(f"ASCII Value of {c} is {ord(c)} ")
    for c in k:
        print(f"Encrypted ASCII Value of {c} is {ord(c)-l} ")
    d= ''
    for c in k:
        d += chr(ord(c)-l) 
        print(f"Here is the encrypted version {chr(ord(c)-l)}")
    print(d)
import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\n")
while True:
    encrypt()
    decrypt_yes_no = input("Do you want to decrypt? enter only 'y' or 'n' ")
    
    if decrypt_yes_no == 'y':
        decrypt()
    elif decrypt_yes_no == 'n':
        break
    else:
        end_it = input("Enter 'q' to end ")
        if end_it == 'q' or end_it == 'Q':
            break
        else:
            continue