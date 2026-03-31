class GrandParent:
    def property(self):
        print("Grandparent owns a house and land")
class Parent(GrandParent):
    def business(self):
        print("Parent runs a family business")
class Child(Parent):
    def education(self):
        print("Child is studying in college")
c = Child()
c.property()    
c.business()    
c.education()  