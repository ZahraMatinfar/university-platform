import csv
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'courses.csv')


def read_db():
    # create list of course objects from database
    courses_list = []
    with open(my_file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            courses_list.append(row)
    return courses_list


def write_db(name, units, total_quantity, teacher_name, course_code, field_code):
    with open(my_file, "a", newline='') as csv_file:
        fieldnames = ['name', 'units', 'total_quantity', 'teacher_name', 'course_code', 'field_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'name': name, 'units': units,
                         'total_quantity': total_quantity, 'teacher_name': teacher_name,
                         'course_code': course_code, 'field_code': field_code})
