import csv

from classes.admin import Admin
from classes.student import Student
from classes.user import User

# create list of class object from database
users_list = []
admins_list = []
students_list = []

with open('../databases/users_db/hash_users_db.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for user in csv_reader:
        user_obj = User(user['username'], user['password'], int(user['user_id']), user['firstname'], user['lastname'],
                        int(user['user_type']), user['field_name'], int(user['field_code']))
        users_list.append(user_obj)
        # if user is student :
        if user['user_type'] == "0":
            student = Student(user['username'], user['password'], int(user['user_id']),
                              user['firstname'], user['lastname'],
                              int(user['user_type']), user['field_name'], int(user['field_code']))
            students_list.append(student)
        # if user is admin
        else:
            admin = Admin(user['username'], user['password'], int(user['user_id']), user['firstname'], user['lastname'],
                          int(user['user_type']), user['field_name'], int(user['field_code']))
            admins_list.append(admin)
