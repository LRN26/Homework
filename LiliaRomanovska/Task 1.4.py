d = {'a': 3, 'cac': 89, 'bc': 5, 'dd': 0}
sorted_ascending = sorted(d.items(), key=lambda item: item[0])  # sorted ascending
sorted_descending = sorted(d.items(), key=lambda item: item[0], reverse=True)  # sorted descending

print(dict(sorted_ascending))
print(dict(sorted_descending))
