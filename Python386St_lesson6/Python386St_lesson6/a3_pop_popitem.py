
d = {"hi": "world", "hi": "world", "hi": "a"}
print(d)
print('----------------')

d = {"1": "world", "2": "a"}
d.pop('1')
print(d)
print('----------------')
d = {"1": "world", "2": "a"}
print(d.pop('1'))

print('----------------')
d = {"1": "world", "2": "a", "3": "b"}
d.popitem()
print(d)
print('----------------')
d = {"1": "world", "2": "a", "3": "b"}
print(d.popitem())
print(d)