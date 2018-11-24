class Person():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def getFullName(self):
        return '{} {}'.format(self.name, self.surname)

pesron = Person('Ola', 'Martyna', 28)
# print(person.getFullName())

class Student(Person):
#    pass
#pass when nothing initialized
    def __init__(self,name,surname,age,isStudent):
        super().__init__(name,surname,age)
        self.isStudent = isStudent
    

student = Student('Kicius', 'Pejsaty', 666, True)
print(student.isStudent)
