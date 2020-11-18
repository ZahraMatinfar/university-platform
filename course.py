class Course:
    def __init__(self, name, units, total_quantity, teacher_name, course_code, field_code):
        """
        remaining_quantity is defined because we need to save total quantity and save changing in another variable
        """
        self.name = name
        self.units = units
        self.total_quantity = total_quantity
        self.remaining_quantity = total_quantity
        self.teacher_name = teacher_name
        self.course_code = course_code
        self.field_code = field_code

    def __str__(self):
        return f'field:{self.field_code}  course:{self.course_code}  unit_number:{self.units}' + \
               f'teacher_name:{self.teacher_name}  total_quantity:{self.total_quantity}  remaining_quantity:{self.remaining_quantity} '

    def __sub__(self, other):
        """
        If the subtraction operator is used, remaining_quantity attribute needs to be changed
        """
        self.remaining_quantity = self.remaining_quantity - other
        return self

    def check_quantity(self):
        """
        Checking the permits for taking the course
        :return: True/False
        """
        if self.remaining_quantity > 0:
            return True
        else:
            return False
