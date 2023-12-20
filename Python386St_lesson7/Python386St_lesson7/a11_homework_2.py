
## ---------------------- ---------------------- ----------------------
## Sets
## ----------------------

a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

print(a)
print(type(a))
print(b)
print(type(b))
print()

## set.pop()
print('.pop() - set')
print(a)
a.pop()
print(a)
print()

## set.discard()
print('.discard() - set')
print(a)
a.discard(5)
print(a)
print()

## set.add()
print('.add() - set')
print(a)
a.add(1)
print(a)

a.add(5)
print(a)
a.add(5)
print(a)
print()


## set.union()
print('.union() - set')
print(a)
print(b)
z5 = a.union(b)
print(z5)
print()


## set.intersection()
print('.intersection() - set')
z6 = a.intersection(b)
print(a)
print(b)
print(z6)
print()

## set.difference()
print('.difference() - set')
z8 = a.difference(b)
print(a)
print(b)
print(z8)
z9 = b.difference(a)
print(z9)
print()

## value in set
print('in set - set')
print(z5)
print(4 in z5)
print(9 in z5)
print(10 in z5)
print()

## set.clear()
print('.clear() - set')
z10 = z9
print(z10)
z10.clear()
print(z10)
print(z9)
print()
print()






## ---------------------- ---------------------- ----------------------
## Tuples
## ----------------------
print("--- Tuples ---")
t = (1, 2, 3, 3, 3, 3, 3, 3)
print(t)
print(type(t))
print(t.count(3))
print(t.index(3))
print()

a, b, c, d, e, f, g, h = t
print(a, b, c, d, e, f, g, h)
a, b, c, d, e, f, g, h = h, g, f, e, d, c, b, a
print(a, b, c, d, e, f, g, h)
print()


x = [(1, 2, 3), (4, 5, 6)]
print(x)
print(type(x))

