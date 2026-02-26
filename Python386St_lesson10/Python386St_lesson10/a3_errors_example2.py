
def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, "use only strings, lists of sets")


s = [1, 2, 3, 4, 4]
u = check_sequence_unique(s)
print(u)

s = 'abcd'
u = check_sequence_unique(s)
print(u)

s = 123
u = check_sequence_unique(s)
print(u)

s = None
u = check_sequence_unique(s)
print(u)

s = False
u = check_sequence_unique(s)
print(u)