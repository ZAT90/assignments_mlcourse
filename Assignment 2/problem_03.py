"""
 Define a tuple containing mixed data types, 
 unpack its values into separate variables, 
 and compare them with another tuple using comparison operators. 
 Then, explain in code comments the main difference between lists and tuples in Python.
"""
tuple1 = ("apple","raspberry",7,5,True, 6.5,False)
(var1,var2,var3,*var4) = tuple1
print(var1)
print(var2)
print(var3)
print(var4)

tuple2 = ("helen","raspberry",12,9,False,"test",True)
print((var1,var2,var3,*var4) == tuple2)
print((var1,var2,var3,*var4) != tuple2)
print((var1,var2,var3,*var4) > tuple2)
print((var1,var2,var3,*var4) < tuple2)

"""
***LIST VS TUPLE***

1. List is mutable. Tuple is immutable.
2. List uses square brackets []. Tuple uses paranthases
3. List is used for a collection of similar items that is flexible. Tuple is used for grouped data that belongs together.
"""

