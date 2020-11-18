import csv

from admin import Admin
from course import Course
from user import User

class Student(User):
    def __init__(self,username, password, user_id, firstname, lastname, user_type, field_name, field_code,entering_year,total_units):
        self.check_admin = True
        self.entering_year=entering_year
        self.total_units=total_units
        super().__init__(self, username, password, user_id, firstname, lastname, user_type, field_name,field_code)


    def __str__(self):
        #show studend information:name/id/total units
        return 'Firstname:{}   Lastname:{}   Entering year:{}   Student ID:{}   Field:{}   \n'.format(self.firstname,self.lastname,self.entering_year,self.user_id,self.field_name)

    def check_units(self):
        if self.total_units>20:
            return 1
        elif self.total_units<10:
            return -1
        else:
            return 0

    def show_available_courses(self):
        #print list of courses defined for student field
        pass
    @staticmethod
    def add_course(self):
        selected_code=input()#course code entered by student
        course=Course(course_code=selected_code)#?
        if self.check_units()==0:
            with open('student_courses.csv', 'a+', newline='') as csv_file:
                fields_names = ['name', 'units', 'total_quantity', 'teacher_name', 'course_code', 'field_name',
                                'field_code']
                writer = csv.DictWriter(csv_file, fieldnames=fields_names)
                writer.writerow({'name': course.name, 'units': course.units, 'total_quantity': course.total_quantity,
                                 'teacher_name': course.teacher_name, 'course_code': course.course_code,
                                 'field_name': course.field_name, 'field_code': course.field_code})



        elif self.check_units()==1:
            pass



    def drop_course(self):
        pass
    @staticmethod
    def show_chosen_courses(self):
        #chosen_courses=[]
        #readlines from file that creat in add_courses and append into chosen_courses
        #print list of courses

        pass

    def submit(self):
        # send chosen courses for admin to approve or reject
        if self.check_units()!=-1 and self.check_units()!=1:
            #with open( csv_file,'r')#read only
            #return file for admin use
            pass

        else:
            pass

    def show_submitted_courses(self):
        if Admin.check_student_course() == self.check_admin:
            self.show_chosen_courses()
        else:
            self.check_admin=False
            print('your request has been rejected')
