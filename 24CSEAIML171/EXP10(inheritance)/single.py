class Person:
    def introduce(self):
        print("Hello, I am Hara")
class Student(Person):
    def study(self):
        print("I am Playing")
s1 = Student()
s1.introduce()   
s1.study()