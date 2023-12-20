
x = [1, 2, 3, 4, 5]

def make_smth(function):
    for element in x:
        print(function(element))


make_smth(lambda a: a + 10)
print()

make_smth(lambda a: a - 4)