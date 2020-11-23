import logging

from run_project.admin_login import admin_login
from run_project.read_databases import users_list, admins_list, students_list
from run_project.student_login import student_login

logging.basicConfig(filename='../msg.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


def user_login(username, password):
    for user in users_list:
        if user.username == username:
            if user.login(username, password):
                user.menu_message()
                logging.info('Successful login')
                successful_login(user)
                break
    else:
        print('\nwrong username or password\n')
        logging.error('Wrong username or password')
        main()


def successful_login(user):
    if user.is_admin():
        for admin in admins_list:
            if admin.user_id == user.user_id:
                while_condition_admin = True
                while while_condition_admin:
                    while_condition_admin = admin_login(admin)
                else:
                    main()
    # if user is student
    else:
        for student in students_list:
            if student.user_id == user.user_id:
                while_condition_student = True
                while while_condition_student:
                    while_condition_student = student_login(student)
                else:
                    main()


def main():
    print('choose an option:\n1.login\n2.exit\n')
    try:
        choice = int(input('your choice:'))
    except ValueError:
        print('invalid input,choose a number in menu. \n')
        logging.exception('invalid input in main function')
        main()
    else:
        if choice == 1:
            username = input('\nEnter your username:')
            password = input('Enter your password:')

            user_login(username, password)

        elif choice == 2:
            print('have a good time')
            logging.info('user exit')
            exit()
        else:
            print('This number is not a number in menu.\n')
            logging.warning('Unavailable option input in menu')
            main()


if __name__ == '__main__':
    main()
