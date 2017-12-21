from Pyproject.test.work6.extends import Student
from Pyproject.test.work6.extends import Teacher
from Pyproject.test.work6.extends import Person


def test(who):
    print(who.Print())


s = Student('student_mick', 18, 98)
# t = Teacher('techar_sir', 32, 6)
# p = Person('ygw', 24)

# test(t)
test(s)
# test(p)
