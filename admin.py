import logging
from user import User
import dtabases.courses.read_corses as db


# logging.basicConfig(filename="msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Admin(User):

    @staticmethod
    def menu_message():
        """
        show menu to admin
        :return: nothing
        """
        print(
            'Please Select an option from the following menu:\n1.logout\n2.Define a course\n3.Show students\n4.Choose student\n6.Check student courses(Pass or Reject)')

    @staticmethod
    def define_course(name, units, total_quantity, teacher_name, course_code, field_code):
        """
        define a course with write function in
        :return: nothing
        """

        db.write_db(name, units, total_quantity, teacher_name, course_code, field_code)
        logging.info("One lesson added!")

    def show_students(self, student):
        """
        Show students list whit specifications
        :param student: Object of Student class
        :return: nothing
        """
        if student.field_code == self.field_code:
            print(student)

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
        if student.submit():  # if student submit courses
            if not status:
                student.take_courses_status = False
                for course in student.chosen_courses:
                    course.remaining_quantity += 1
                student.chosen_courses = []
                student.total_units = 0
                logging.warning("Rejected")
            else:
                student.take_courses_status = True
                logging.info("Passed")
        else:  # if student didn't submit courses
            student.take_courses_status = False
            for course in student.chosen_courses:
                course.remaining_quantity += 1
            student.chosen_courses = []
            student.total_units = 0
            logging.warning("Rejected")
