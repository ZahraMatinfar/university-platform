"""
we need courses_list to generate our objects later.
"""
import csv

def read_db():
    courses_list = []
    with open('courses.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            courses_list.append(row)
    return courses_list

def write_db(name,units,total_quantity,teacher_name,course_code,field_code):
    with open('courses_list.csv', 'a+', newline='') as csv_file:
        fieldnames = ['name', 'units', 'total_quantity', 'teacher_name', 'course_code', 'field_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'name': name ,'units': units,
                         'total_quantity': total_quantity, 'teacher_name': teacher_name,
                         'course_code': course_code, 'field_code':field_code})
