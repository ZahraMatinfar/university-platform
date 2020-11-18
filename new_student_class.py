from user import User


class Student(User):
    def __init__(self,username, password, user_id, firstname, lastname, user_type, field_name, field_code,
                 total_units):
        self.check_admin = True

        self.total_units = total_units
        super().__init__(username, password, user_id, firstname, lastname, user_type, field_name, field_code)
    def show_available_courses(self,field_code,courses_list):
        std_courses=[]
        for course in courses_list:
            if self.field_code==course.field_code:
                std_courses.append(course)
    @staticmethod
    def add_course(self,course_code,courses_list):

