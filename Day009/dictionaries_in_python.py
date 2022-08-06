import art
print(art.text2art("dict", font='block'), art.text2art("ion", font='block'),art.text2art("ary", font='block'))
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Adding new items to dictionary
programming_dictionary['Loop'] = 'The action of doing smth over and over again'
#Retrieving from dictionary
#print(programming_dictionary['Bug'])
for c in programming_dictionary.keys():
    
    print(c)
    #print("*"*50)
    print(programming_dictionary[c])

print("*"*50)
# Empty dictionary
fruits = {}
fruits['Apple']= 2.99
print(programming_dictionary, fruits)
