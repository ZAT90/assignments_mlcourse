"""
Create a function that accepts two sets as parameters and 
returns their union, intersection, and difference. 
Use keyword arguments with default parameter values so the function 
can work even if one of the sets is not provided by the user. Display the results clearly.
"""

def setCalculations(set1={1,2},set2={"a","b",1}):
    print('set1: ',set1)
    print('set2: ',set2)
    # union
    resultUnion = set1.union(set2)
    print('union',resultUnion)
    # intersection
    resultIsection = set1.intersection(set2)
    print('resultIsection: ',resultIsection)

    # difference
    resultDifference = set1.difference(set2)
    print('resultDifference: ',resultDifference)
    return {"union":resultUnion,"intersection":resultIsection, "difference":resultDifference}


print(f"printing all results: {setCalculations({"a","b","c"},{"d","c","b","f"})}")