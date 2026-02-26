
my_dict = { 'key': 'value',
           10    :  True,
           0.2    : 'hello'}
print(my_dict)
print(my_dict['key'])
print(my_dict[10])
print(my_dict[0.2])
print('------------')
#print(my_dict[15])
print(my_dict.get(15))
print(my_dict.get(0.2))
print(my_dict.get('key2', -1))
print(my_dict.keys())
#my_dict.clear()
#print(my_dict)
