import logging

from prettytable import PrettyTable

from classes.user import User
import databases.course.read_courses as db


class Admin(User):

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
        define a course with write function in
        :return: nothing
        """

        db.write_db(name, units, total_quantity, teacher_name, course_code, field_code)

    def show_students(self, students_list):
        """
        Show students list whit specifications
        :param students_list: list of Student in same field with admin
        :return: nothing
        """
        t = PrettyTable(['id', 'first name', 'last name', 'field name', 'field code'])
        for student in students_list:
            if student.field_code == self.field_code:
                t.add_row(
                    [student.user_id, student.first_name, student.last_name, student.field_name, student.field_code])
        print(t)

    @staticmethod
    def choose_student(user_id, student):
        """
        Choose student with id and then show selected units and lessons
        :param user_id: id for selected user that admin want to see lessons
        :param student: Object of Student class
        :return: nothing
        """
        # for user in students_list:
        if student.user_id == user_id:
            for lesson in student.chosen_courses:
                print(lesson)

    @staticmethod
    def check_student_course(student, status):
        """
        Check student courses and pass or reject
        :param student: object of Student class
        :param status: admin status for pass(True) or reject(False)
        :return: nothing
        """
        if student.submit():  # if student submitted her courses
            if not status:  # if number of student units are not acceptable
                student.take_courses_status = False
                logging.error("Courses Rejected")
            else:
                student.take_courses_status = True
                logging.info("Courses Submitted")
        else:  # if student didn't submit courses
            student.take_courses_status = False
            logging.error("Courses not Submitted")
