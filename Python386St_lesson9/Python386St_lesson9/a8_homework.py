
### First tast (change global "x")
### -----------------------------

#x = 15
#print(x)

#def x_glob_change(y):
#    x = y
#    return x

#print(x)
#x = x_glob_change(6)
#print(x)




## Second tast (recursion, factorial)
## -----------------------------
#def func_factorial(x):
#    if x == 1:
#        return 1
#    else: 
#        return x * func_factorial(x - 1)


#print(func_factorial(3))




### Third tast (build-in function)
### -----------------------------

#def external(x):
#    def internal():
#        return x ** 2

#    return internal()


#print(external(3))





### Fourth tast (max in list - recursion)
### -----------------------------

def max_list(x, max1=None):
    if max1 is None:
        max1 = x.pop()
    elem = x.pop()
    if elem > max1:
        max1 = elem
    if x:
        return max_list(x, max1)
    return max1


sw = [1, 2, 5, 3, -3, 25, 26.5]
print(max_list(sw))