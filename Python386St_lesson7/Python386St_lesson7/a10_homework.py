
## First task: difference, intersection, union
##-----------------------
#A = {3, 5, 11, 7, 4, -3}
#B = {11, 5, 8, 1, 10, 7}
#print(B.difference(A))

#print(A.intersection(B))
#print(B.intersection(A))

#print(A.union(B))






### Second task: unique string- method list and set
###-----------------------
#string = "a14wbwfh"
#list1 = list(string)
#set1 = set(string)
##print(list1)
##print(set1)
##print(list1[2:])

#x1 = None
#counter = 0
#for i in list1:
#    if i in list1[counter+1:]:
#        print("This string isn't unique (method list)")
#        x1 = False
#        break
#    else:
#        x1 = True
#    counter += 1
#if x1:
#    print("This string is unique (method list)")


#print('----------------------')
#string2 = ''
#for i in set1:
#    string2 += i
    
#print(string)
#print(string2)
#if len(string) == len(string2):
#    print("this string is unique (method set)")
#else:
#    print("This string isn't unique (method set)")








### Third task: set method
###-----------------------
#my_set = {1, 2 , 3 , 4, 'a', 'b', 'c', 'd'}
#print(my_set)
#print()

#print("1) delet first set's element (set_name.pop):")
#my_set.pop()
#print(my_set)
#print()

#print("2) delet set's element 'value' (set_name.remove):")
#my_set.remove(2)
#print(my_set)
#print()

#print("3) delet set's element 'value' (set_name.discard):")
#my_set.discard(2)
#print(my_set)
#print()

#print("4) add element 'value' in end set (set_name.add):")
#my_set.add(2)
#print(my_set)
#print()

#print("5) add element 'value' in end set (set_name.add):")
#my_set.add(2)
#print(my_set)
#print()

#print("6) add set in end set (set_name.union):")
#new_set = {10, 11, 12, 13, 14, 15, 2, 3}
#my_set1 = my_set.union(new_set)
#print(my_set1)
#print()

#print("7) intersection set1 end set (set_name.intersection):")
#my_set2 = my_set.intersection(new_set)
#print(my_set2)
#print()

#print("8) different set1 end set (set_name.difference):")
#my_set2 = my_set.difference(new_set)
#print(my_set2)
#print()

#print("9) elemetn in set ('a' in set):")
#my_set3 = 4 in my_set
#print(my_set3)
#print()

#print("10) clear set (set_name.clear()):") 
#my_set.clear()
#print(my_set)
#new_set.clear()
#print(new_set)




### Fourth task: tuple method
###-----------------------
my_tuple = (1, 5, 5, 8)
a, b, c, d = my_tuple
print('Tuple in val"a,b,c,d":',a, b, c, d)

a, b, c, d = d, c, b, a
print('Reverse val"a,b,c,d":',a, b, c, d)

my_tuple2 = (a, b, c, d)
if my_tuple == my_tuple2:
    print("it's Ttue")
else:
    print("it's False")
print('--------------')

a = [(1, 2, 3, 4), (7, 8, 9, 0)]
print(a)
print(type(a), 'lenght list:', len(a),'(tuples)')
a1 = a[1]
print(type(a1), 'lenght tuple:', len(a1))
print()

print('"a" in tuple')
for first, second, third, fourth in a:    
    print(first, second, third, fourth)