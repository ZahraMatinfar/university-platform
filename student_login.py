from run import *


def student_login(student):
    student.menu_message()
    choice = int(input('your choice:'))

    # menu: 1.Offered courses in current semester.2.Take course.3.Drop course4.Student courses.5.Submit courses.6.logout

    if choice == 1:
        student.defined_available_courses()

    elif choice == 2:
        student.show_available_courses()
        student.add_course(course_code=input('course code:'))
        logging.info('Student added a new course')

    elif choice == 3:
        student.show_chosen_courses()
        student.drop_course(course_code=input('course code:'))
        logging.info('Student dropped a course')

    elif choice == 4:
        student.show_chosen_courses()

    elif choice == 5:
        student.submit()
        logging.info('Student submitted courses')
        student.show_submitted_courses()

    elif choice == 6:
        student.logout()
        logging.info('Student logout')
        main()
    else:
        logging.warning('invalid input')