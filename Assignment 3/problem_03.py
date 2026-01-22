"""
Define a class that shows encapsulation by using private attributes 
and public getter/setter methods. 
Add two methods with the same name but different parameter counts 
to illustrate method overloading (using default arguments). 
Then create another class to demonstrate multiple inheritance.
"""

class Home:
    def __init__(self,setter_home):
        self.__setter_home = setter_home
    
    def getter_home(self):
        return self.__setter_home
    
    def setter_home(self,newHome):
        self.__setter_home = newHome
    
    def displayDetails(self,owner=None,age=None):
        if owner is not None and age is not None:
           print(f"you are {owner} age is {age}")
        elif owner is not None:
            print(f"you are {owner} with no age")
        else:
            print("no info given")
    

myhome = Home("10 downing street")
print(myhome.getter_home())

myhome.setter_home("12th K Avenue")
myhome.displayDetails("john",12)
myhome.displayDetails()
myhome.displayDetails("Rose")

class HousingCompany:
    def displayCompanyMessage(self):
        print('we are the best housing company in the country')


class MultiInheritance(Home,HousingCompany):
    pass

testMulti = MultiInheritance("107 block C")
print(testMulti.getter_home())
testMulti.displayCompanyMessage()
testMulti.displayDetails("Rakib",45)