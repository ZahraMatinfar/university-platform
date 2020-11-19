import csv
import dtabases.users
from admin import Admin

from student_class import Student

admins = []
students = []
file_path = 'hash_users_db.csv'
with open(file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for user in csv_reader:
        if user['user_type'] == '0':
            user = Student(user['username'],user['password'],user['firstname'],user['lastname'],user['user_id'],user['user_type'],user['field_name'],user['field_code'])
            students.append(user)
        else:
            admin = Admin(user['username'],user['password'],user['firstname'],user['lastname'],user['user_id'],user['user_type'],user['field_name'],user['field_code'])
            admins.append(user)

def show_students():
    for student in students:
        admin.show_students(student)

def choose_student():
    user_id = input("Inter User ID")
    for student in students:
        admin.choose_student(user_id,student)

def check_student_course():
    status = input("Inter Status of Student Courses")
    for student in students:
        admin.check_student_course(status,student)

