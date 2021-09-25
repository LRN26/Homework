import csv


def get_top_performers(file_path, number_of_top_students=5):

    """function receives file path and returns names of top performer students"""

    with open(file_path, 'r') as students_info:
        reader = csv.DictReader(students_info)
        students_sorted = sorted(reader, key=lambda students_dict: float(students_dict['average mark']), reverse=True)
    return [name["student name"] for name in students_sorted[:number_of_top_students]]


print(get_top_performers(r'C:\Users\Lenovo\Downloads\data\students.csv', 5))


def descending_order_of_age(filepath):
    """Implement a function which receives the file path with students info
     and writes CSV student information to the new file in descending order of age."""

    with open(filepath, "r") as students_info:
        with open(filepath, "a", newline="") as students_age_sorted:
            reader = csv.reader(students_info)
            writer = csv.writer(students_age_sorted)
            writer.writerow(next(reader))
            sorted_students = sorted(reader, key=lambda student: student[1], reverse=True)
            writer.writerows(sorted_students)


print(descending_order_of_age(r'C:\Users\Lenovo\Downloads\data\students.csv'))
