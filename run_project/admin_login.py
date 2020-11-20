from run_project.read_databases import students_list
import logging
import re

logging.basicConfig(filename="../msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def admin_login(admin):
    global chosen_student
    admin.menu_message()
    try:
        choice = int(input('your choice:'))
        # menu: Please Select an option from the following menu:1.Define a course.2.Show students.3.Choose student.4.logout

        if choice == 1:
            admin.define_course(name=input('course name:'), units=input('course units:'),
                                total_quantity=input('total quantity:'), teacher_name=input('teacher name:'),
                                course_code=input('course code:'), field_code=input('field code:'))
            print('\ncourse is defined successfully.\n')
            logging.info("New course defined!")

        elif choice == 2:
            admin.show_students(students_list)

        elif choice == 3:
            admin.show_students(students_list)
            user_id = int(input('Enter the student\'s id:'))
            for student in students_list:
                chosen_student = admin.choose_student(user_id, student)
            print('\nDo you want to change student courses status(Pass or Reject)?\n1.yes\n2.no')
            change = re.sub(r"\s+", "", input('>>>').lower(), flags=re.UNICODE)
            answer = {'y': ['y', '1', '1.y', '1.yes', 'yes'], 'n': ['n', '2', '2,n', '2.no', 'no']}
            if change in answer['y']:
                admin.check_student_course(chosen_student, status=input('Student course take status:'))
            elif change in answer['n']:
                pass
            else:
                print('invalid input')

        elif choice == 4:
            admin.logout()
            logging.info('Admin logout')
            return False
        else:
            print('The number of your choice is not in menu')
    except ValueError:
        print('invalid input,choose a number.\n')
        logging.warning('invalid input in admin login')
    return True