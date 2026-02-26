
# first letter key (name) != 'a"
d = {"alice": 35, "mark": 25, "aprel": 45, "john":19}
print("Dictionary:", d)
new_d ={}
for name, age in d.items():
    if name[0] != 'a':
        new_d[name] = age
print(new_d)