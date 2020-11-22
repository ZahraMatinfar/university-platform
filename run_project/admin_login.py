import logging
import re

from run_project.read_databases import students_list

logging.basicConfig(filename='../msg.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


def admin_login(admin):
    """

    :param admin: an object of Admin class
    :return: True if student choose an option from menu and False if she logout
    """
    admin.menu_message()
    try:
        choice = int(input('your choice:'))
    except ValueError:
        print('invalid input,choose a number.\n')
        logging.warning('invalid input in admin login')
    else:
        # menu: Please Select an option from the following menu:1.Define a course.2.Show students.3.Choose student.4.logout
        if choice == 1:
            try:  # check input type for int
                name = input('course name:')
                units = input('course units:')
                total_quantity = input('total quantity:')
                teacher_name = input('teacher name:')
                course_code = input('course code:')
                field_code = input('field code:')
                if name and int(units) and int(total_quantity) and teacher_name and int(course_code) and int(
                        field_code) != '':  # check inputs are not empty
                    admin.define_course(name, units, total_quantity, teacher_name, course_code, field_code)
                    print('\nCourse is defined successfully.\n')
                    logging.info("New course defined!")
                else:
                    print('\nInputs are incomplete! ')
                    logging.error('Inputs are incomplete')
            except ValueError:
                print('\nValue of your input information is incorrect\n')
                logging.error('Value of your input information is incorrect')
            except TypeError:
                print("Type of your input is incompatible")
                logging.error("Type of your input is incompatible")


        elif choice == 2:
            admin.show_students(students_list)

        elif choice == 3:
            admin.show_students(students_list)
            try:
                user_id = int(input('Enter the student\'s id:'))
                for student in students_list:
                    if student.user_id == user_id and student.field_code == admin.field_code:
                        admin.choose_student(user_id, student)
                        print('\nDo you want to change student courses status(Pass or Reject)?\n1.yes\n2.no')
                        change = re.sub(r"\s+", "", input('>>>').lower(), flags=re.UNICODE)
                        answer = {'y': ['y', '1', '1.y', '1.yes', 'yes'], 'n': ['n', '2', '2,n', '2.no', 'no']}
                        if change in answer['y']:
                            print('What is your choice for student\'s course take status?:\n1.Agree\n2.Reject')
                            status = re.sub(r"\s+", "", input('your choice:').lower(), flags=re.UNICODE)
                            possible_answer = {'1': ['1.agree', 'agree', '1'], '2': ['2.reject', 'reject', '2']}
                            if status in possible_answer['1']:
                                admin.check_student_course(student, True)
                                print('status changed successfully.')
                                logging.info(f'Admin changed {student.user_id} status to True ')
                            elif status in possible_answer['2']:
                                admin.check_student_course(student, False)
                                print('status changed successfully.')
                                logging.info(f'Admin changed {student.user_id} status to False ')
                            else:
                                print('invalid input.')
                        elif change in answer['n']:
                            pass
                        else:
                            print('invalid input')
                        break
                else:
                    print('No student have this id.')
            except ValueError:
                print("Value of your input is incorrect")
                logging.error("Value of your input is incorrect")
            except TypeError:
                print("Type of your input is incompatible")
                logging.error("Type of your input is incompatible")

        elif choice == 4:
            admin.logout()
            logging.info('Admin logout')
            return False
        else:
            print('The number of your choice is not in menu')
    return True
