class User:
    def __init__(self, username, password, user_id, firstname, lastname, user_type, field_name, field_code):
        """
        login status is False/True .False means User is not logged in   &  True means User is logged in successfully
        :param username: username
        :param password: password
        :param user_id: Personnel Code/student code
        :param firstname: firstname
        :param lastname: lastname
        :param user_type: 0/1 .0 for student ,1 for admin
        :param field_name:field name
        :param field_code:a code for field
        """
        self.username = username
        self.password = password
        self.login_status = "False"
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.user_type = user_type
        self.field_name = field_name
        self.field_code = field_code

    def login(self, user_input, pass_input):
        """
        if user_input & pass_input is correct,user will login successfully.
        :param user_input: a username
        :param pass_input: a password
        :return: login status
        """
        if self.username == hash(user_input) and self.password == hash(pass_input):
            self.login_status = "True"
        return self.login_status

    def logout(self):
        """
        by calling this method login status will change to False(The user exits the messenger)
        :return: login status
        """
        self.login_status = "False"
        return self.login_status

    @staticmethod
    def menu_message():
        """
        show menu to user
        :return: nothing
        """
        print('     welcome to University Automation\n')
        print('Please Select an option from the following menu:\n')
        print('1.login\n2.logout')

    def is_admin(self):
        """
        check user is admin or not.
        :return: True/False
        """
        if self.user_type == '1':
            return True
        else:
            return False
