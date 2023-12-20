
my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]
print("my_list:", my_list)

value_to_count = 1
count_dict = {value_to_count: 0}
for element in my_list:
    if element == value_to_count:
        count_dict[value_to_count] += 1
print(count_dict)
print('1) ----------------')
print()


count_dict = {}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
print(count_dict)
print('2) ----------------')
print() 


count_dict = {}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
for key, value in count_dict.items():
    print("Key:", key, "count-", value)