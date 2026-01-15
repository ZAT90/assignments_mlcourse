"""
Write a Python program that takes a list of numbers as input, 
removes duplicates using a suitable list method, 
and returns a dictionary containing the original list, the unique values, and their count. 
Use a function with parameters and a return statement to perform this task.
"""

def organizeList(inputItems):
    print(f"splitted list: {inputItems}")

    isAllNum = all(x.isdigit() for x in inputItems)
    if not isAllNum: return print('All input must be numbers')
    
    noDupList = list(dict.fromkeys(inputList))
   
    dictToReturn = {"original_list": inputItems, "unique_items":noDupList, "unique_count": len(noDupList)}
    print(dictToReturn)
    return dictToReturn


inputList = input("Enter numbers seperated by space: ").split()
print(f"return statement using function: {organizeList(inputList)}")
