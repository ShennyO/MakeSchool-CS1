class Student(object):
    """docstring for Student."""
    def __init__(self, name):
        # super(Student, self).__init__()
        self.name = name
        self.GPA = None
        self.assignments = {}

    def add_assignment(self,name):
        self.assignments[name] = None

    def update_assignment(self,name,grade):
         if name in self.assignments:
             self.assignments[name] = grade

    def remove_assignment(self,name):
        if name in self.assignments:
            self.assignments.pop(name)

    def get_GPA():
        temp_GPA = 0
        for x in self.assignments:
            temp_GPA += self.assignments[x]
        self.GPA = temp_GPA
