## ---------------------- ---------------------- ----------------------
## Dctionary
## ----------------------
my_dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
    }
print(my_dict)
print()

## dict.get[key]
print('.get[key] - dict')
print(my_dict.get('5'))
print()

## dict.items()
print('.items() - dict')
print(my_dict.items())
print(type(my_dict.items()))
print()

## dict.pop()
print('.pop() - dict')
print(my_dict)
print(my_dict.pop('1'))
print(my_dict)
print(my_dict.pop('9'))
print(my_dict)
print()

## dict.popitem()
print('.popitem() - dict')
print(my_dict)
z2 = my_dict.popitem()
print(z2)
print(my_dict)
print()

## dict.update()
print('.update() - dict')
print(my_dict)
my_dict.update({'1': 100})
print(my_dict)
print()


## dict.values()  .keys()
print('.values() .keys() - dict')
print(my_dict.values())
z4 = my_dict.values()
print(z4)
print(my_dict.keys())
print(type(my_dict.keys()))
list1 = list(my_dict.keys())
print(type(list1))
print(list1.sort())
print()

## dict.clear()
print('.clear() - dict')
print(my_dict)
my_dict_1 = my_dict
my_dict_1.clear()
print(my_dict)
print(my_dict_1)
print()





