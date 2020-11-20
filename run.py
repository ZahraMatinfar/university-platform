

import csv
import logging

from admin import Admin
from admin_login import admin_login
from user import User
from student import Student
# from admin_login import admin_login
from student_login import student_login

logging.basicConfig(filename="msg.log", filemode='a', level=logging.WARNING, format='%(asctime)s - %(message)s')

users_list = []
admins = []
students = []

with open('hash_users_db.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for user in csv_reader:
        user_obj = User(user['username'], user['password'], user['firstname'], user['lastname'], int(user['user_id']),
                        int(user['user_type']), user['field_name'], int(user['field_code']))
        users_list.append(user_obj)
        if user['user_type'] == '0':
            student = Student(user['username'], user['password'], user['firstname'], user['lastname'],
                              int(user['user_id']),
                              int(user['user_type']), user['field_name'], int(user['field_code']))
            students.append(student)
        else:
            admin = Admin(user['username'], user['password'], user['firstname'], user['lastname'], int(user['user_id']),
                          int(user['user_type']), user['field_name'], int(user['field_code']))
            admins.append(admin)


def user_login(username, password):
    for user in users_list:
        if user.login(username, password):
            successful_login(user)
            logging.info('Successful login')
    else:
        # print('wrong username or password')
        logging.error('Wrong username or password')


def successful_login(user):
    if user.is_admin():
        for admin in admins:
            if admin.user_id == user.user_id:
                admin_login(admin)
                break
    else:
        for student in students:
            if student.user_id == user.user_id:
                student_login(student)
                break


def main():
    username = input('Enter your username:')
    password = input('Enter your password:')
    user_login(username, password)


if __name__ == '__main__':
    main()

