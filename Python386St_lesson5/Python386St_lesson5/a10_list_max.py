
x = [3, 2, 1, 7, 0, -3, 25, -78, 45, 100, -1, 10]
max_element = x[0]
for element in x:
    if element > max_element:
        max_element = element

min_element = x[0]
for element in x:
    if element < min_element:
        min_element = element

print(max_element)
print(min_element)
max_element= max(x)
print(max_element)
