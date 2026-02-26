
x = 1
print(x)


def print_x():
    x = 10
    print(x)

print_x()


def get_x():
    x = 20
    return x


x_from_local = get_x()
print(x_from_local)