import dtabases.courses.read_courses as db

from user import User


# logging.basicConfig(filename="msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Admin(User):
    def menu_message(self):
        """
        show menu to admin
        :return: nothing
        """
        print(
            'Please Select an option from the following menu:\n1.logout\n2.Define a course\n3.Show students\n4.Choose student\n6.Check student courses(Pass or Reject)')

    def define_course(self, name, units, total_quantity, teacher_name, course_code, field_code):
        """
        define a course with write method
        :return: nothing
        """

        db.write_db(name, units, total_quantity, teacher_name, course_code, field_code)

    def show_students(self, students_list):
        """
        Show students list whit specifications
        :param students_list: list of students in all fields
        :return: nothing
        """
        for user in students_list:
            if user.field_code == self.field_code:
                print(user)

    def choose_student(self, user_id, students_list):
        """
        Choose student with id and then show selected units and lessons
        :param user_id: id for selected user that admin want to see lessons
        :param students_list: list of students in all fields
        :return: nothing
        """
        for user in students_list:
            if user.user_id == user_id:
                for lesson in user.chosen_courses:
                    print(lesson)

    def check_student_course(self, student, status):
        """
        Check student courses and pass or reject
        :param student: object of Student class
        :param status: admin status for pass(True) or reject(False)
        :return: nothing
        """
        if not status:
            student.status = False
