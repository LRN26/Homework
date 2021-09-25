"""sort the names and write them to a new file"""

file = open(r'C:\Users\Lenovo\Downloads\data/unsorted_names.txt', 'r')
file_sorted = open(r'C:\Users\Lenovo\Downloads\data/sorted_names.txt', 'w')
lines = sorted(file.readlines())
file_sorted.writelines(lines)
print(*lines)
file.close()
file_sorted.close()

