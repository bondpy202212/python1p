def get_max_from_list(list_values):
    max_value = list_values[0]
    for element in list_values:
        if element > max_value:
            max_value = element
    return max_value if max_value > 0 else "Max value less the zero"



a = [1, 3, 56, 45, 0]
max_a = get_max_from_list(a)
print(max_a)
print('--------------------')
print(max(a))

a = [-45, -2, -89, -78]
max_a = get_max_from_list(a)
print(max_a)


