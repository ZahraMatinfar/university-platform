import csv

from user import User
from course import Course
import logging
from write_courses import write_courses


# from student_class import Student


# logging.basicConfig(filename="msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Admin(User):
    students_list = r'D:\maktabsharif\python_project\university-platform\dtabases\users\users_db.csv'

    def __init__(self, username, password, user_id, firstname, lastname, user_type, field_name, field_code):
        super().__init__(username, password, user_id, firstname, lastname, user_type, field_name, field_code)

    def menu_message(self):
        """
        show menu to admin
        :return: nothing
        """
        super().menu_message()
        print('3.Define a course\n4.Show students\n5.Choose student\n6.Check student courses(Pass or Reject)')

    def define_course(self, name, units, total_quantity, teacher_name, course_code, field_code):
        """
        define a course with method's attributes
        :return: nothing
        """

        # reference to Course class
        # course = Course(name, units, total_quantity, teacher_name, course_code, field_code)
        # write_courses(
        #     {'name': course.name, 'units': course.units, 'total_quantity': course.total_quantity,
        #      'teacher_name': course.teacher_name, 'course_code': course.course_code,
        #      'field_code': course.field_code})

        self.name = name
        self.units = units
        self.total_quantity = total_quantity
        self.remaining_quantity = total_quantity
        self.teacher_name = teacher_name
        self.course_code = course_code
        self.field_code = field_code
        # write_courses(self.name, units, total_quantity, teacher_name, course_code, field_name, field_code)
        write_courses(
            {'name': self.name, 'units': self.units, 'total_quantity': self.total_quantity,
             'teacher_name': self.teacher_name, 'course_code': self.course_code,
             'field_code': self.field_code})
        # log add a lesson
        # logging.info("a lesson is added")

    def show_students(self):
        # Show students list whit specifications
        with open(self.students_list, 'r') as stu_list:
            reader = csv.DictReader(stu_list)
            for row in reader:
                print(row['username'], row['password'], row['firstname'], row['lastname'], row['user_id'],
                      row['user_type'], row['field_name'], row['field_code'])

    def choose_student(self, user_id):
        # choose student with id and then show selected units and lessons
        self.user_id = user_id
        with open(self.students_list, 'r') as stu_list:
            reader = csv.DictReader(stu_list)
            for row in reader:
                if row['user_id']==user_id:
                    pass
                    # show lessons
                return True
            else:
                return False

    # check student courses and pass or reject
    def check_student_course(self, status):
        self.status = status
        if self.status is True:
            logging.info("Passed")
            print("Check Student Course : Passed")
            # change a variable in student class
        else:
            logging.info("Rejected")
            print("Check Student Course : Rejected")
        return status


# a = Admin('35111113', '4210ab', '35111113', 'Nastaran', 'Magham', '1', 'Biomedical engineering', '33')
# a.menu_message()
# # a.define_course('Farsiiiii', '3', '7', 'Afrasiab', '115', '0')
# a.show_students()
# a.choose_student('95991311')
