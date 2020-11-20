import logging

logging.basicConfig(filename="../msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def student_login(student):
    student.menu_message()
    student.defined_available_courses()
    try:
        choice = int(input('your choice:'))

        # menu: 1.Offered courses in current semester.2.Take course.3.Drop course4.Student courses.5.Submit courses.6.logout

        if choice == 1:
            student.show_available_courses()

        elif choice == 2:
            take = student.add_course(course_code=int(input('course code:')))
            if take is None:
                print('course quantity is complete.')
                logging.warning('Try take full course.')
            elif take:
                student.show_chosen_courses()
                logging.info('Student added a new course')
            else:
                print('This course already has been chosen by you .')

        elif choice == 3:
            student.show_chosen_courses()
            if student.drop_course(course_code=input('course code:')):
                print('Course dropped successfully')
                logging.info('Student dropped a course')
            else:
                print('Code is not valid.')

        elif choice == 4:
            student.show_chosen_courses()

        elif choice == 5:
            if student.submit():
                print('submission is successfully.')
                logging.info('Student submitted courses')
                student.show_submitted_courses()
            else:
                print('You can\'t submit.Your unit number is low or too much. ')

        elif choice == 6:
            student.logout()
            print('logout successfully\n')
            logging.info('Student logout')
            return False
        else:
            print('The number of your choice is not in menu')
    except ValueError:
        print('invalid input,choose a number .\n')
        logging.warning('invalid input in student login')

    return True
