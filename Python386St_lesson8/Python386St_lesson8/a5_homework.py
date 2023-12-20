
### First task (integer numbers a, b)
### --------------------------------------
#def func_two_int(a, b):
#    if type(a) != int or type(b) != int:
#        print("numbers a, b isn't integer")
#        print('-----')
#        return 1
#    elif type(a) == int and type(b) == int:
#        if a + b > 0:
#            print("a + b >= 0")
#            print('-----')
#            return 0
#        elif a + b ==0:
#            print("a + b == 0")
#            print('-----')
#            return -2
#        else:
#            print("a + b < 0")
#            print('-----')
#            return -1

#print(func_two_int(-1., -1))







### Second task (function(function))
### --------------------------------------
#def func_second(a, b):
#    return a + b


#def func_first(x):
#    print("start call")    
#    print("Sum a + b :", x)
#    print("finish call")
    

#a = 1 
#b = 3
#x = func_second(a, b)
#func_first(x)




## Third task (greatest common divisor)
## --------------------------------------
def g_c_d(a, b):
    if type(a) != int or type(b) != int:
        print('Please enter integer a, b.')
        print()
    else:        
        set_a = set()
        set_b = set()
        for i in range(1, a + 1):
            if  a % i == 0:                
                set_a.add(i)
            
        for j in  range(1, b + 1):
            if b % j == 0:
                set_b.add(j)
            
        #print(set_a)
        #print(set_b)
        #print(max(set_a.intersection(set_b)))
        return max(set_a.intersection(set_b))

print(g_c_d(20, 100))
