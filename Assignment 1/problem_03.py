"""
Problem: 03
Write a program using a for loop that calculates the sum of even numbers between 1 and 100.

"""



sum_numbers = 0
first_num = 1
last_num = 100

for i in range(first_num,last_num+1):
    if i % 2 == 0:
        sum_numbers += i

print(sum_numbers)