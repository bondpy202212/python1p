
## First task: max value in dict
##----------------
#d = {'a': 3, 'b': 168, 'd': -3}

#new_d = []
#for key, value in d.items():
#    new_d.append(value)
#print(max(new_d))
#print(max(d.values()))




## Second task: max value in dict
##----------------
#d = {'a': 3, 'b': 'hello', 'c': 1253, 'd': -3}

#new_d = []
#for key, value in d.items():
#    if type(value) == int or type(value) == float:
#        new_d.append(value)
#print(max(new_d))




## Third task: methods distionary
##----------------
d = {1: 'a', 2: 'b', 3:'c', 4: 'd', 5: 'e'}
print("Print 'value' in dict for key = 2:\n", d[2])
print("-- \\ -- method .get()    key = 2:\n", d.get(2))
print("-- \\ -- method .get()    key = 0:\n", d.get(0))
#print("dict.clear :", d.clear())
print("Delete element dict for key = 2:\n", d.pop(2))
print(d)
print("Delete end element dict.popitem():\n", d.popitem())
print(d)
print("Add element in dict.update({:}):\n", d.update({8: 'f'}))
print(d)
print("Print values like a list- dict.value():\n", d.values())

print("Print (key: values) like a list- dict.items():\n", d.items())