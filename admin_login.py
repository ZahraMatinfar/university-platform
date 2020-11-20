from run import *


def admin_login(admin):
    global chosen_student
    admin.menu_message()
    choice = int(input('your choice:'))
    # menu: Please Select an option from the following menu:1.Define a course.2.Show students.3.Choose student.4.Check student courses(Pass or Reject).5.logout

    if choice == 1:
        admin.define_course(name=input('course name:'), units=input('course units:'),
                            total_quantity=input('total quantity:'), teacher_name=input('teacher name:'),
                            course_code=input('course code:'), field_code=input('field code:'))
        logging.info("New course defined!")

    elif choice == 2:
        admin.show_students(students)

    elif choice == 3:
        user_id = input('Enter the student\'s id:')
        for student in students:
            chosen_student = admin.show_students(user_id, student)
        if choice == 4:
            admin.check_student_course(chosen_student, status=input('Student course take status:'))

    elif choice == 4:
        print('first choose a student')  # warning
        logging.info('first choose a student')

    elif choice == 5:
        admin.logout()
        logging.info('Admin logout')
        main()
    else:
        logging.warning('invalid input')