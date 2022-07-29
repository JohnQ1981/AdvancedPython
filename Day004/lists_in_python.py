import random
names = ['Salih', 'Hilola', 'Muhammad', 'Zayd', 'Ihsan', 'John']
print(names)
names.append('Qosimi')
print(names)

family = ['Qosim', 'Mubarak', 'Komil', 'Ilhom', 'Nigora']
names.extend(family)
print(names)

ran = random.choice(names)
print(ran)

print(names[-2])