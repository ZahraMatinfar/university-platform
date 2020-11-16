from user import User
from course import Course
import logging
from write_courses import write_courses

logging.basicConfig(filename="msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Admin(User):
    students_list = r'D:\maktabsharif\python_project\university-platform\dtabases\users\users_db'

    def __init__(self, field, username, password, user_id, firstname, lastname, user_type, field_name, field_code):
        super().__init__(username, password, user_id, firstname, lastname, user_type, field_name, field_code)

    @staticmethod
    def menu_message():
        """
        show menu to admin
        :return: nothing
        """
        super().menu_message()
        print('3.Define a course\n4.Show students\n5.Choose student\n6.Check student courses(Pass or Reject)')

    def define_course(self, name, units, total_quantity, teacher_name, course_code, field_name, field_code):
        """
        define a course with method attributes
        :return: nothing
        """
        self.name = name
        self.units = units
        self.total_quantity = total_quantity
        self.remaining_quantity = total_quantity
        self.teacher_name = teacher_name
        self.course_code = course_code
        self.field_code = field_code
        self.field_name = field_name
        # write_courses(self.name, units, total_quantity, teacher_name, course_code, field_name, field_code)
        write_courses(
            [self.name, self.units, self.total_quantity, self.remaining_quantity, self.teacher_name, self.course_code,
             self.field_code, self.field_name])
        # log add a lesson
        logging.info("a lesson is added")

    @staticmethod
    def show_students(self):
        # Show students list whit specifications

        with open(self.students_list, 'r') as f:
            print(f.readlines())

    def choose_student(self, user_id):
        # choose student with id and then show selected units and lessons
        self.user_id = user_id
        with open(self.students_list, 'r') as f:
            lines = f.readline()
            for line in lines:
                if str(id) in line:
                    print(line)
                    # show lessons
            else:
                print("there is not student whit this id")

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
