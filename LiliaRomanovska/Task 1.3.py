str_1 = [i.strip() for i in input().lower()]
d = dict()
for i in str_1:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(dict(sorted_d))
