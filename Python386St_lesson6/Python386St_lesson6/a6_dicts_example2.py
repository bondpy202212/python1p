
d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

for key, value in d.items():
    if key % 2 == 0:
        print(key, value)