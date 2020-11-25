import logging
import re

from run_project.read_databases import students_list

logging.basicConfig(filename='../msg.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


def admin_login(admin):
    """
    call Admin class methods depending on witch option selected by admin in menu
    MENU : 1.Define a course2.Show students3.Choose student4.logout
    :param admin: an object of Admin class
    :return: True if admin choose an option from menu and False if she logged out
    """
    # print menu for admin
    admin.menu_message()
    try:
        choice = int(input('your choice:'))
    except ValueError:
        print('invalid input,choose a number.\n')
        logging.exception('invalid input in admin login')
    else:
        # menu options:
        if choice == 1:
            try:
                name = input('course name:')
                units = input('course units:')
                total_quantity = input('total quantity:')
                teacher_name = input('teacher name:')
                course_code = input('course code:')
                field_code = input('field code:')

                # check inputs are not empty
                if name and int(units) and int(total_quantity) and teacher_name and int(course_code) and int(
                        field_code) != '':
                    # admin can define courses just for his field
                    if admin.field_code == int(field_code) or field_code == '0':
                        define_course= admin.define_course(name, units, total_quantity, teacher_name, course_code, field_code)
                        if define_course:
                            print('New course is defined successfully.\n')
                            logging.info("New course defined!")
                        else:
                            print('This course has been defined already')
                            logging.warning('Try define existing course')
                    else:
                        print("You can not define  any course for other fields!!")
                        logging.warning("Try defined course for other fields")
                else:
                    print('Fields can not be empty please enter course information')
                    logging.error('Empty input for define course')
            except ValueError:
                print('invalid inputs.\n')
                logging.error('Invalid input in admin menu')
            except TypeError:
                print("Input type unacceptable,Enter suitable values")
                logging.error("Unacceptable input type in define course")

        elif choice == 2:
            admin.show_students(students_list)

        elif choice == 3:
            admin.show_students(students_list)
            try:
                user_id = int(input('Enter the student\'s id:'))
                for student in students_list:
                    if student.user_id == user_id and student.field_code == admin.field_code:
                        # just show information of submitted courses
                        if admin.choose_student(user_id, student):
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
                                print('Invalid input')
                                logging.error('Invalid input.')
                            break
                        # if student.check_submission() is False
                        else:
                            print("No course submitted")
                            logging.warning('Try see student information before submission ')
                            break
                else:
                    print('No student found with this id')
                    logging.error('Try search unavailable student id')
            except ValueError:
                print('invalid input,Enter a number .\n')
                logging.error('invalid input.[Try choose student]')
            except TypeError:
                print('Input type unacceptable,Enter suitable values')
                logging.error("Unacceptable input type in choose student")
        elif choice == 4:
            admin.logout()
            logging.info('Admin logout')
            return False
        else:
            print('The number of your choice is not in menu')
            logging.error('Unavailable option input in admin menu')
    return True
