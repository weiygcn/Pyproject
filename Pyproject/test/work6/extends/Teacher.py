from Pyproject.test.work6.extends.Person import Person


class Teacher(Person):
    def __init__(self, name, age, level):
        super(Teacher, self).__init__(name, age)
        self.level = level

    def Print(self):
        return 'I am:', self.name, ' is ', self.age, 'years old,level is:', self.level
