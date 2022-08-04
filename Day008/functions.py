def greet(name):
  print(f'Hola {name}')
  print(f'Hello {name}')
  print(f'Namaste {name}')

def great_2(name , location):
    print(f'Hola {name}. What is it Like in {location}')
    print(f'Hello {name}. What is it Like in {location}')
    print(f'Namaste {name}. What is it Like in {location}')

def great_unlimited(name,  location, *args):
    print(f'Hola {name}. What is it Like in {location}, zip: {args}')
    print(f'Hello {name}. What is it Like in {location}')
    print(f'Namaste {name}. What is it Like in {location}')
#while True:
greet('John')
great_2('Tolly', 'New York')
great_unlimited('John', 'New York', 652)