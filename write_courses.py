import csv

courses_list = r'D:\maktabsharif\python_project\university-platform\dtabases\courses\courses.csv'


def write_courses(course_attributes):
    with open(courses_list, 'a+', newline='') as csv_file:
        fieldnames = ['name', 'units', 'total_quantity', 'teacher_name', 'course_code', 'field_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'name': course_attributes['name'], 'units': course_attributes['units'],
                         'total_quantity': course_attributes['total_quantity'], 'teacher_name': course_attributes['teacher_name'],
                         'course_code': course_attributes['course_code'], 'field_code': course_attributes['field_code']})
