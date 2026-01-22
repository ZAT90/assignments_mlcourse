"""
Create a Python class representing a student with attributes such as name and ID, 
and include both a default constructor and a parameterized constructor. 
Add a method to display the student details, 
and use the pass statement inside an empty placeholder method. 
Then create multiple objects from this class to test each constructor.
"""

class StudentInfo:
    def __init__(self,name=None,id=None):
        self.name = name
        self.id = id
    
    def displayDetails(self):
        if self.name is not None and self.id is not None:
           print(f"you are {self.name} and id is {self.id}")
        elif self.name is not None:
            print(f"you are {self.name} with no id")
        else:
            print("no info given")
    
    def testEmptyPlaceHolder():
        pass

stu1 = StudentInfo("john",12)
stu1.displayDetails()

stu2 = StudentInfo()
stu2.displayDetails()

stu3 = StudentInfo("Rose")
stu3.displayDetails()