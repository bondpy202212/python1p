
#### First task (division by zero)
#### -----------------------------
#def divide_two(x,y):
#    return x / y


#def try_divizion(x,y):
#    try:
#        return divide_two(x,y)
#    except ZeroDivisionError as zero_error:
#        print(zero_error, ", 'y' can't be = 0")
#        return 0

#print(try_divizion(4, 0))





### Second task (element in list)
### -----------------------------
def found(list1, elem):
    x = list1[elem]
    return x


def found_elem_list(list, elem):
    try:
        return found(list, elem)
    except TypeError as type_error:
        print(type_error, ", use only strins or lists")
        return -2
    except BaseException as base_error:
        print(base_error, ", this element isn't in list")
        return -1


x = [1, 2, 3, 4, 5]
#x = 125
print('------------')
elem = 5
print(x)
print('------------')
print(found_elem_list(x, elem))
