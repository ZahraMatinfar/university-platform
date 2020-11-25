import json
import logging

from prettytable import PrettyTable

import databases.course.read_courses as db
from classes.user import User


class Admin(User):
    """
    a child class of User class thar play role of education administrator
    ATTRIBUTES: attributes of User class
    METHODS: menu_massage,define_course,show_students,choose_student,check_student_course
    """

    @staticmethod
    def menu_message():
        """
        show menu to admin
        :return: nothing
        """
        print(
            '\nPlease Select an option from the following menu:\n1.Define a course\n2.Show students\n3.Choose student\n4.logout\n')

    @staticmethod
    def define_course(name, units, total_quantity, teacher_name, course_code, field_code):
        """
        define a course with write_db function in read_courses module
        :return: False if course has been defined already else True
        """
        courses= db.read_db()
        for course in courses:
            if str(course_code) == course['course_code']:
                return False
        else:
            db.write_db(name, units, total_quantity, teacher_name, course_code, field_code)
            return True
    def show_students(self, students_list):
        """
        Show students list whit specifications.
        :param students_list: list of Student with same field with admin creat in read_databases file
        :return: nothing
        """
        table = PrettyTable(
            ['id', 'first name', 'last name', 'field name', 'field code'])
        for student in students_list:
            if student.field_code == self.field_code:
                table.add_row(
                    [student.user_id, student.first_name, student.last_name, student.field_name, student.field_code])
        print(table)

    @staticmethod
    def choose_student(user_id, student):
        """
        Choose student by student id and show her courses information
        :param user_id: user_id for student that admin want to see her courses
        :param student: Object of Student class
        :return: nothing
        """
        if student.user_id == user_id:
            if student.check_submission():
                student.show_submitted_courses()
                return True
            else:
                return False
    @staticmethod
    def check_student_course(student, status):
        """
        Check student courses and approve or reject them
        :param student: object of Student class
        :param status: admin status for approve(True) or reject(False)
        :return: nothing
        """
        if student.check_submission():# if student submitted her courses
            if not status:
                with open('../databases/users_db/students_info.json') as std_info:
                    info = json.load(std_info)
                    student_info = info[f'{student.user_id}']
                    student_info[0]['courses_status'] = False
                    info.update(student_info[0])
                with open('../databases/users_db/students_info.json', 'w') as std_info:
                    json.dump(info, std_info)
                logging.error("Reject student courses")
            else:
                with open('../databases/users_db/students_info.json') as std_info:
                    info = json.load(std_info)
                    student_info = info[f'{student.user_id}']
                    student_info[0]['courses_status'] = True
                    info.update(student_info[0])
                # with open('../databases/users_db/students_info.json', 'w') as std_info:
                #     json.dump(info, std_info)
                logging.info("Approve student courses ")
        else:  # if student didn't submit her courses
            logging.error('Try check student courses before submission')
