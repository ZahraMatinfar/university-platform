import csv
import json

from classes.course import Course
from classes.user import User
from databases.course.read_courses import read_db
from prettytable import PrettyTable
import pandas as pd

class Student(User):
    # initialize student attributes
    def __init__(self, username, password, user_id, first_name, last_name, user_type, field_name, field_code):
        self.take_courses_status = None
        self.total_units = 0
        self.chosen_courses = []
        super().__init__(username, password, user_id, first_name, last_name, user_type, field_name, field_code)

    # overload str method for print student information
    def __str__(self):
        return super().__str__() + f'  total units:{self.total_units}'

    def __iadd__(self, other):
        self.total_units += other

    def __isub__(self, other):
        self.total_units -= other

    @staticmethod
    def menu_message():
        """
        show menu to user
        :return: nothing
        """
        print('\nPlease Select an option from the following menu:\n')
        print(
            '1.Offered courses in current semester\n2.Take course\n3.Drop course\n4.Student courses\n5.Submit courses\n6.Logout\n')

    def check_units(self):
        """
        check number of student units
        :return: 0 for acceptable number/1 for more than allowed number/-1 for less than allowed number
        """
        if self.total_units > 20:
            return 1
        elif self.total_units < 10:
            return -1
        else:
            return 0

    def defined_available_courses(self):
        """
        select list of defined courses for student field from all courses
        :return: nothing
        """

        available_courses = []
        courses_list = read_db()
        for course in courses_list:
            if self.field_code == int(course['field_code']) or int(course['field_code']) == 0:
                available_courses.append(
                    Course(course['name'], int(course['units']), int(course['total_quantity']), course['teacher_name'],
                           int(course['course_code']), int(course['field_code'])))
        return available_courses

    def show_available_courses(self):
        """
        print available courses for student when 'Offered courses in current semester' option  in menu selected
        :return:nothing
        """

        table = PrettyTable(
            ['course code', 'course name', 'units', 'teacher name', 'field code', 'total quantity'])

        for lesson in self.defined_available_courses():
            table.add_row(
                [lesson.course_code, lesson.name, lesson.units, lesson.teacher_name, lesson.field_code,
                 lesson.total_quantity])
        print(table)

    def add_course(self, course_code):
        """
        add specified course in student chosen_courses list when 'Take course' option selected from menu
        :param course_code:
        :return: True if course have enough quantity,else:False.None If course is chosen already.
        """

        for course in self.defined_available_courses():

            # self.available_courses contains list of Course objects
            if course_code == course.course_code:
                # check that course has enough quantity
                if course.check_quantity:
                    if course in self.chosen_courses:
                        return None
                    else:
                        course.remaining_quantity -= 1
                        self.total_units += course.units
                        self.chosen_courses.append(course)
                        return True
                else:
                    return False

    def drop_course(self, course_code):
        """
        delete specified course in student chosen_courses list when 'Drop course' option selected from menu
        :param course_code
        :return: True if course dropped .False if course didnt choose already
        """
        for course in self.chosen_courses:
            if course_code == course.course_code:
                course.remaining_quantity += 1
                self.total_units -= course.units
                self.chosen_courses.remove(course)
                return True
            else:
                return False

    def show_chosen_courses(self):
        """print student chosen courses"""
        if len(self.chosen_courses) == 0:
            print('No courses have been added yet.')
        else:
            table = PrettyTable(
                ['course code', 'course name', 'units', 'teacher name', 'field code', 'total quantity'])

            for lesson in self.chosen_courses:
                table.add_row(
                    [lesson.course_code, lesson.name, lesson.units, lesson.teacher_name, lesson.field_code,
                     lesson.total_quantity])
            print(table)

    def submit(self):
        """
        final step of take course is submit courses and save them in the file
        so admin can check and approve or reject them
        :return: True if number of units are between 10 and 20/else:False
        """


        if self.check_units() != -1 and self.check_units() != 1:
            with open('../databases/users_db/students_info.json') as std_info:
                json_data = json.load(std_info)
                student_dict = {f'{self.user_id}': [vars(course) for course in self.chosen_courses]}
            json_data.update(student_dict)
            with open('../databases/users_db/students_info.json', 'w') as std_info:
                json.dump(json_data, std_info)
            return True
        else:
            return False

    def show_submitted_courses(self):
        """
        after submit courses show final chosen courses depending on that admin approve or reject them
        :return:nothing
        """

        if self.take_courses_status:
            with open('../databases/users_db/students_info.json') as std_info:
                info = json.load(std_info)
                table = PrettyTable(['course code', 'course name', 'units', 'teacher name', 'field code', 'total quantity'])
                for course in info[f'{self.user_id}']:
                    values = []
                    for i in ['course_code', 'name', 'units', 'teacher_name', 'field_code', 'total_quantity']:
                        values.append(course[i])
                    table.add_row(values)
                print(table)
        else:
            print('your request has been rejected')
