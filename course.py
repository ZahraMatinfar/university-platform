class Course:
    def __init__(self, name, units, total_quantity, teacher_name, course_code,field_name,field_code):
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
        self.field_name = field_name

    def __str__(self):
        """
        self.field_code+self.course_code is a code that users for take courses.
        :return: a string
        """
        return '    {0}      {1}  {2}  {3}     {4}    {5}'.format(self.field_code+self.course_code, self.name, self.units,
                                                                  self.teacher_name, self.total_quantity,
                                                                  self.remaining_quantity)

    def __sub__(self, other):
        self.remaining_quantity = self.total_quantity - other

    def check_quantity(self):
        """
        Checking the permits for taking the course
        :return: True/False
        """
        if self.remaining_quantity > 0:
            return True
        else:
            return False
