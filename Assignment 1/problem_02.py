"""
Problem: 02
Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

"""


operators = ["+","-","*","/"]

def myCalculator():
    num1 = input_num('first number: ')
    num2 = input_num('second number: ')
    operator = input('What operation do you want? Only + , - , * , / is allowed: \n')


    if num1.isnumeric() and num2.isnumeric():
     if operator in operators:
      expression = f"{num1}{operator}{num2}"
      calculation = eval(expression)
      print(calculation)
     else:
        print('wrong operator used')
    else:
       print('both input must be number')

def input_num(message):
    input_num = input(f'Please input {message}: ')
    return input_num
  



myCalculator()
