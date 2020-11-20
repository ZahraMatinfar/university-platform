import logging

logging.basicConfig(filename="../msg.log", filemode='a', level=logging.DEBUG, format='%(ascetic)s - %(message)s')


def student_login(student):
    """
    call Student class methods depending on witch option selected by student in menu
    menu: 1.Offered courses in current semester.2.Take course.3.Drop course4.Student courses.5.Submit courses.6.Logout
    :param student:
    :return: True if student choose an option from menu and False if she logout
    """
    # print menu for student
    student.menu_message()
    try:
        choice = int(input('your choice:'))
        if choice == 1:
            # show available courses that defined for student field
            student.defined_available_courses()
            student.show_available_courses()

        elif choice == 2:
            available_courses = student.defined_available_courses()
            if len(available_courses) == 0:
                print('No courses have been defined for you yet')
                logging.warning('Try take course before courses defined')

            else:
                take = student.add_course(course_code=int(input('course code:')))
                # if quantity of course is complete,take returned False
                if not take:
                    print('course quantity is complete.')
                    logging.warning('Try take full course.')
                # if course didnt choose already by student and have enough quantity,take is True
                elif take:
                    student.show_chosen_courses()
                    logging.info('Student added a new course')
                # if take is None:
                else:
                    print('This course already has been chosen by you .')

        elif choice == 3:
            student.show_chosen_courses()
            if student.drop_course(course_code=input('course code:')):
                print('Course dropped successfully')
                logging.info('Student dropped a course')
            else:
                print('Code is not valid.')
                logging.warning('invalid course code for dropping')

        elif choice == 4:
            if student.submit():
                student.show_submitted_courses()
            else:
                student.show_chosen_courses()

        elif choice == 5:
            if student.submit():
                print('submission is successfully.')
                logging.info('Student submitted courses')
                student.show_submitted_courses()
            else:
                print('You can\'t submit.Your unit number is low or too much. ')
                logging.warning('Student unsuccessful submission')

        elif choice == 6:
            student.logout()
            print('logout successfully\n')
            logging.info('Student logged out')
            return False
        else:
            print('Unavailable option,choose another number!')

    except ValueError:
        print('invalid input,choose a number .\n')
        logging.warning('invalid input in student menu')

    return True
