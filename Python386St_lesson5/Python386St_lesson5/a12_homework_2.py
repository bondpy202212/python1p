
## List
## ----------------------

a_letter = ['a', 'b', 'c', 'd']
a_number =[1, 2, 3, 4, 5, 6]
a_bool = [True, False, True]
a_symbol = ['asdf', '#', '%', '&', 'kl']
a_kit = [1, '2', 'd', True, 'hello', '*']

# slicing
print('slicing - list')
print(a_letter[0:3:2])
print(a_letter[0:10:1])
print(a_number[1:])
print(a_number[::-1])
print(a_number[:0:-1])
print()

# .append
print('.append - list')
a_number.append(-100)
print(a_number)
print()

# .clear
print('.clear - list')
print(a_number)
a_number_cl = a_number
a_number_cl.clear()
print(a_number_cl)
print(a_number)
print()

# .extend
print('.extend - list')
a_number_plus = [10, 11, 12, 13, 14, 15]
print(a_letter)
a_letter.extend(a_number_plus)
print(a_letter)
print()

# .pop
print('.pop - list')
z1 = a_letter.pop()
print(z1)
print(a_letter)
z2 = a_letter.pop(4)
print(z2)
print(a_letter)
print()

# .index
print('.index - list')
print(a_letter)
print(a_letter.index('a'))
print(a_letter.index(12))
print()

# .reverse
print('.reverse - list')
a_letter.reverse()
print(a_letter)

# .sort
print('.sort - list')
a_letter_1 = a_letter[:4]
print(a_letter_1)
a_letter_1.sort()
print(a_letter_1)
a_letter_1.sort(reverse = True)
print(a_letter_1)
print()





## string
## ----------------------
string = 'abcdefgh'
print(string)
print(string[::-1])
print(string[:6:])
print(string[:6:2])

print(string.index('d'))
print(string)






