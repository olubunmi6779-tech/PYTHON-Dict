my_dict = {}

my_dict = {1: 'Orange', 2:'YoYo'}

my_dict = {'name': 'Kate', 1:[3,6,9]}

my_dict = {'name': 'Kate', 'age': 24}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 28
print(my_dict)

my_dict['address'] = 'Lagos'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)