
# Type error
#    BaseException
#    NameError
#    TypeError
#    ValueError
#    AssertionError
#    ImportError


## BaseException
## ------------------
a = 10
b = 0
try:
    c = a / b
except BaseException:
    c = 0
    print("division on zero")
print(c)
print('-------------')
print('1) BaseException')
print('-------------')
print()





## NameError
## ------------------
def x():
    d = 10


try:
    print(d)
except ValueError as error:
    print(error)
except NameError as error:
    print(error)
print('-------------')
print('2) NameError')
print('-------------')
print()





## ValueError
## ------------------
try:
    print('sdf')
except ValueError as error:
    print(error)
print('-------------')
print('3) ValueError')
print('-------------')
print()





## AssertionError
## ------------------
try:
    assert 2 == 3
except AssertionError as error:
    print(error)
print('-------------')
print('4) AssertionError')
print('nothing print, but if "assert 2 == 3"')
#assert 2 == 3
print('-------------')
print()





## TypeError
## ------------------
x1 = None
try:
    for elem in x1:
        print(elem)
except TypeError as error:
    print(error)
print('-------------')
print('5) TypeError')
print('-------------')
print()