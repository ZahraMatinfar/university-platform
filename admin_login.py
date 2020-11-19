from run import *


def admin_login(admin):
    global chosen_student
    admin.menu_message()
    choice = int(input('your choice:'))

    if choice == 1:
        admin.define_course(name=input('course name:'), units=input('course units:'),
                            total_quantity=input('total quantity:'), teacher_name=input('teacher name:'),
                            course_code=input('course code:'), field_code=input('field code:'))
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

    elif choice == 5:
        admin.logout()
        main()
    else:
        print('invalid input')  # warning
