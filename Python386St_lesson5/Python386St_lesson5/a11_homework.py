
### First task (numbers > 5)
### -----------------------
#x = [2, 4, 65, 32, 2, 6, 0, -1, 3]
#for elem in x:
#    if elem > 5:
#        print(elem)





#### Second task (palindrom)
#### -----------------------
#word = "aabfbaa"
#print("This word '{}' is polindrom or not?".format(word))
#print()

#is_polindrom = None
#for elem in range(len(word)):
#    #print(word[elem])
#    #print(word[-1 -elem])

#    if word[elem] != word[-1 -elem]:
#        print("This word isn't palindrom")
#        print()
#        break
#    else:
#        is_polindrom = True
#if is_polindrom:
#    print("This word is palindrom")
#    print()
###-------------------------------------



## Third task (numbers > 6)
## -----------------------
#a_list = [1, 3, 9, 13, 7, 8, 32, 44, 59, 19]
#for a in a_list:
#    if a > 6:
#        print(a)
## -----------------------




## Fourth task (Extra in list "a")
## -----------------------
a = ['red', 'yellow', 'blue', 'bread', '123']
red = ['red', 'yellow', 'blue']

for i in a:
    if i not in red:
        print()
        print("This element '{}' isn't a color".format(i))
        print()
