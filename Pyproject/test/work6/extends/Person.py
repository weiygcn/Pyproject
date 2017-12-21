class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Print(self):
        return '<person> my name is ',self.name,' is ',self.age,' years old'