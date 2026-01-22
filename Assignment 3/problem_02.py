"""
Write a Python program demonstrating single, multilevel, and hierarchical inheritance 
using simple classes such as Person, Student, and Teacher. 
Include at least one overridden method in the child classes to show method overriding.
"""

class Person:
    def workStyle(self):
        print("A person goes to his destination in the morning")

# Single and multiple inheritance
class Student(Person):
    pass

class Teacher(Person):
    pass

# multilevel inheritance
class Police(Person):
    def worksLikePolice(self):
        print("A policeman goes to work in morning but his working hours are not fixed")

class TrafficPolice(Police):
    def trafficStyle(self):
        print("works in the road to maintain safety and discipline")



student = Student()
student.workStyle()

teacher = Teacher()
teacher.workStyle()

traffic = TrafficPolice()
traffic.trafficStyle()
traffic.worksLikePolice()
traffic.workStyle()