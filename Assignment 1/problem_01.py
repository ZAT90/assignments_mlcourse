"""
Problem: 01 
Write a Python program that takes a number as input and checks whether it is even or odd.

"""

def numberChecker():
    my_input = input('Please input a number: ')

    if my_input.isnumeric():
        check_val = int(my_input)
        if check_val % 2 == 0:
         print('number is even')
        else:
         print('number is odd')
    else:
       print('must input number only')
    
   

numberChecker()