dirty_dozen_mixed = ['Strawberries','Spinach','Kale','Nectarines','Apples','Grapes','Peaches','Cherries','Pears','Tomatoes','Celery','Potatoes']
fruits = ['Strawberries', 'Nectarines', 'Apples','Grapes','Peaches','Cherries','Pears',]
vegatables= []
for c in dirty_dozen_mixed:
    if c  not in fruits:
        vegatables.append(c)

print(vegatables)
vegatables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

dirty_dozen = fruits + vegatables
print(dirty_dozen)
dirty_dozen2 = [fruits, vegatables]
print(dirty_dozen2)

#print(dirty_dozen)
print(len(dirty_dozen), len(dirty_dozen_mixed))