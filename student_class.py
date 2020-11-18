import csv

from admin import Admin
from course import Course
from user import User


class Student(User):
    def __init__(self,username, password, user_id, firstname, lastname, user_type, field_name, field_code):
        self.check_admin = True
        self.total_units = 0
        self.available_courses=[]
        self.chosen_courses=[]
        super().__init__(username, password, user_id, firstname, lastname, user_type, field_name, field_code)

    def __str__(self):
        # show student information:name/id/total units
        return super.__str__() + str(self.total_units)

    @staticmethod
    def menu_message():
        """
        show menu to user
        :return: nothing
        """
        print('Please Select an option from the following menu:\n')
        print('1.Offered courses in current semester\n2.Take course\n3.Drop course\n4.Student courses\n5.Submit courses\n')

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

    def define_available_courses(self):
        """
        print list of defined courses for student field

        """
        # csv_file = csv.reader(open('courses.csv', "r"), delimiter=",")
        # # search courses in file by matching field codes
        # for row in csv_file:
        #     if self.field_code == row[5]:
        #         print(row)

        courses_list =read_db()#it should be return of read_courss.py read_db func #remember import
        self.available_courses=[]
        for course in courses_list:
            if self.field_code == course['field_code'] or course['field_code']==0:
                self.available_courses.append(Course(course['name'],course['units'],course['total_quantity'],course['techer_name'],course['course_code'],course['field_code']))
        return self.available_courses
    def show_available_courses(self):
        for course in self.available_courses:
            print(course)

    def add_course(self,course_code):
        # with open('student_chosen_courses.csv', 'a', newline='')as std_courses:
        #     fieldnames = ['name', 'units', 'total_quantity', 'teacher_name', 'course_code', 'field_code']
        #     writer = csv.DictWriter(std_courses, fieldnames=fieldnames)
            # search courses in file by matching field codes

        for row in self.available_courses:
            if course_code == row.course_code:
                if row.check_quantity:
                    row.remaining_quantity -=1
                    self.chosen_courses.append(row)
                    return True
                else:
                    return False


                # writer.writerow({'name': row, 'units': row[1],
                #                      'total_quantity': row[2], 'teacher_name': row[3],
                #                      'course_code': row[4], 'field_code': row[5]})







    def drop_course(self,course_code):
        for row in self.available_courses:
            if course_code == row.course_code:
                row.remaining_quantity += 1
                self.chosen_courses.remove(row)

    def show_chosen_courses(self):
        # print list of courses
        for course in self.chosen_courses:
            print(course)

    def submit(self):
        # send chosen courses for admin to approve or reject
        if self.check_units() != -1 and self.check_units() != 1:
            # with open( csv_file,'r')#read only
            # return file for admin use

            with open('student_chosen_courses.csv', 'a', newline='')as std_courses:
                fieldnames = ['student_id','courses']
                writer = csv.DictWriter(std_courses, fieldnames=fieldnames)
                for row in self.chosen_courses:
                    course_info=[row.name,row.units,row.total_quantity,row.teacher_name,row.course_code,row.field_code]
                    writer.writerow({'student_id':self.user_id,'courses':course_info})
            return True

        else:
            return False


    def show_submitted_courses(self):
        if self.check_admin:
            self.show_chosen_courses()
        else:
            print('your request has been rejected')
