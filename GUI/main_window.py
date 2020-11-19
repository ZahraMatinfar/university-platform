# from tkinter import *
from GUI.login_window import *
def push_btn():
    login()
    main_screen.destroy()

main_screen = Tk()
main_screen.geometry("300x250")  # set the configuration of GUI window
main_screen.title("Account Login")
# create a Form label
Label(text="Choose Login Or Logout", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# create Login Button
login_btn=Button(text="Login", height="2", width="30", command=push_btn).pack()
Label(text="").pack()
#login_btn.bind('<Button-1>', push_btn(main_screen))
# create a register button
# Button(text="Logout", height="2", width="30").pack()

main_screen.mainloop()  # start the GUI


# call the main_account_screen() function
