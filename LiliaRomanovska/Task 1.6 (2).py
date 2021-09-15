a = 2
b = 4
c = 3
d = 7
for i in range(c, d + 1):
    print('\t', i, end=' ')
print()
for i in range(a, b + 1):
    print(i, end=' ')
    for j in range(c, d + 1):
        print('\t', i * j, end=' ')
    print()
