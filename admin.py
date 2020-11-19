from user import User
import databases.course.read_corses as db


# logging.basicConfig(filename="msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Admin(User):
    @staticmethod
    def menu_message():
        """
        show menu to admin
        :return: nothing
        """
        print(
            'Please Select an option from the following menu:\n1.Define a course\n2.Show students\n3.Choose student\n4.Check student courses(Pass or Reject)\n5.logout')

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

    def choose_student(self, user_id, student):
        """
        Choose student with id and then show selected units and lessons
        :param user_id: id for selected user that admin want to see lessons
        :param students_list: list of students in all fields
        :return: nothing
        """

        if student.user_id == user_id:
            for lesson in student.chosen_courses:
                print(lesson)
        return student
    def check_student_course(self, student, status):
        """
        Check student courses and pass or reject
        :param student: object of Student class
        :param status: admin status for pass(True) or reject(False)
        :return: nothing
        """
        if not status:
            student.status = False

# user = Admin('username', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '95991385', 'zahra',
#             'matin', 1, 'c', 11)
# user.define_course('a','b','c','d','e','f')
# # admin=Admin(*user)
# print(admin.login('username','password'))