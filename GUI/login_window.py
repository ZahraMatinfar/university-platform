from tkinter import messagebox
from tkinter import *
from user import User
from admin import Admin



def login():
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    # global username_verify
    # global password_verify

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()


def login_verification():
    # get username and password

    username = username_login_entry.get()
    password = password_login_entry.get()

    # this will delete the entry after login button is pressed
    # username_login_entry.delete(0, END)
    # password_login_entry.delete(0, END)
    user = User('username', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '95991385', 'zahra',
                'matin', 0, 'c', 11)

    if user.login(username, password):
        successful_login(user)
    else:
        messagebox.showwarning(title='unsuccessful login', message='wrong username or password')

# def unsuccessful_login():

def successful_login(user):
    if user.is_admin():
        admin = Admin(user)
    # else:
    #     student=Student(user)
