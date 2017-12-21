from Pyproject.test.work6.extends.Person import Person


class Student(Person):
    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score

    def Print(self):
        return 'I am:', self.name, ' is ', self.age, 'My score is:', self.score
