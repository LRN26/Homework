line = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = set()
for dict in line:
    for val in dict.values():
        s.add(val)
print(s)
