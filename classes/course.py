class Course:
    """
    ATTRIBUTES: name, units, total_quantity,remaining_quantity, teacher_name, course_code, field_code
    METHODS:init,str,sub,check_quantity
    """
    def __init__(self, name, units, total_quantity, teacher_name, course_code, field_code):
        self.name = name
        self.units = units
        self.total_quantity = total_quantity
        # remaining quantity is equal to total quantity at first
        self.remaining_quantity = total_quantity
        self.teacher_name = teacher_name
        self.course_code = course_code
        self.field_code = field_code

    def __str__(self):
        # overload str method for print course information
        return f'field:{self.field_code}  course code:{self.course_code}  unit_number:{self.units}' + \
               f'  teacher_name:{self.teacher_name}  total_quantity:{self.total_quantity}' + \
               f'  remaining_quantity:{self.remaining_quantity} '

    def __sub__(self, other):
        """
        If the subtraction operator is used, remaining_quantity attribute needs to be changed
        """
        self.remaining_quantity = self.remaining_quantity - other
        return self

    def check_quantity(self):
        """
        Checking the permits for taking the course
        :return: True if the course has enugh quantity,else False
        """
        if self.remaining_quantity > 0:
            return True
        else:
            return False
