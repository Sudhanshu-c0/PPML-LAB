class Parent:
    def show(self):
        print("parent class")
class Child(Parent):
    def show(self):
        print("child class")
Parent_obj=Parent()
Child_obj=Child()
Parent_obj.show()
Child_obj.show()

