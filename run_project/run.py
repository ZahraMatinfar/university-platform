import logging
from run_project.read_databases import users_list, admins_list, students_list
from run_project.student_login import student_login
from run_project.admin_login import admin_login

logging.basicConfig(filename="../msg.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def user_login(username, password):
    for user in users_list:
        if user.login(username, password):
            user.menu_message()
            successful_login(user)
            logging.info('Successful login')
            break
    else:
        print('\nwrong username or password\n')
        logging.warning('Wrong username or password')
        main()


def successful_login(user):
    if user.is_admin():
        for admin in admins_list:
            if admin.user_id == user.user_id:

                while admin_login(admin):
                    admin_login(admin)
                else:
                    main()
                break
    else:
        for student in students_list:
            if student.user_id == user.user_id:
                while student_login(student):
                    student_login(student)
                else:
                    main()
                break


def main():
    print('choose an option:\n1.login\n2.exit\n')
    try:
        choice = int(input('your choice:'))
    except ValueError:
        print('invalid input,choose a number in menu.\n')
        logging.exception('invalid input in main function')
        main()
    else:
        if choice == 1:
            username = input('\nEnter your username:')
            password = input('Enter your password:')

            user_login(username, password)

        elif choice == 2:
            print('have a good time')
            exit()
        else:
            print('This number is not a number in menu.\n')
            main()


if __name__ == '__main__':
    main()
