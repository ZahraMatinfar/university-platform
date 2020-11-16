class Student(User):
    def __init__(self):
        self.field=field
        self.entering_year=entering_year
        self.total_units=total_units
        self.chosen_courses=[]
        #self.submited_courses=()
        super().__init__(self)

    def __str__(self):
        #show studend information:name/id/total units
        return 'Firstname:{}   Lastname:{}   Entering year:{}   Student ID:{}   Field:{}   \n'.format(self.first_name,self.last_name,self.entering_year,self.id,self.field)
        #check if i should overload chosen courses

    def check_units(self):
        if self.total_units>20:
            return 1
        elif self.total_units<10:
            return -1
        else:
            return 0

    def add_course(self):
        #append course to chosen_courses by course code
        if check_units()==0:
            course_code=int(input('corse code: '))
            course=Course(course_code)#check
            self.chosen_courses.append(course)
            #loggig.info()
        elif check_units()==1:
            #logging.basicConfig('')
            #logging.Warning('')
            #print(something)

    def drop_course(self):
        #remove course from chosen_courses by course code
        course_code = int(input('corse code: '))
        course = Course(course_code)  # check
        self.chosen_courses.remove(course)
        #log



    def show_available_courses(self):
        #print list of courses defined for student field

        pass

    def show_chosen_courses(self):
        #print list of courses
        pass

    def submit(self):
        # send chosen courses for admin to approve or reject
        if check_units()!=-1 and check_units()!=1:
            # we can covert it to a tuple for make it immutable(check dont make problem for admin)
            self.submited_courses=tuple(chosen_courses)
        else:
            #lOGGIN.basicConfig()
            #logging.ERROR
            #print('')



