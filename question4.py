# Modular Calculator ➗
# Write a calculator using the math module that contains the following features:

# Objective:
# Write a function called pow that takes inputs a and b and returns the power
# Write a function called ceiling that takes input a returns math.ceil
# Write a function called floor that takes input a returns math.floor
# Write a function called factorial that takes input a returns math.factorial
# Use the variables a and b below as needed for each function

import math 
from math import pow
# , ceil, floor, factorial

def pow(a,b):
    return a**b

def ceiling(a):
    return math.ceil(a)

def flooring(a):
    return math.floor(a)

def factorialing(a):
    return math.factorial(a)

def modularCalculator():
    functionUsed = input("What operation are you performing (Exponential, Ceiling, Floor, Factorial) ? ")

    print("function:",functionUsed)
    functionUsed.strip()

    if (functionUsed == "Exponential") or (functionUsed == "exponential"):
        a = int(input("Input a value for 'a': "))
        b = int(input("Input a value for 'b': "))
        print("The power of",a,"to the",b, "is", pow(a,b))  
    else:
        a = int(input("Input a number: "))
        if (functionUsed == "Ceiling") or (functionUsed == "ceiling"):
            print("Ceiling of",a,"is",ceiling(a))
        elif (functionUsed == "Floor") or (functionUsed == "floor"):
            print("Floor of",a,"is",flooring(a))
        elif (functionUsed == "Factorial") or (functionUsed == "factorial"):
            print("Factorial of",a,"is",factorialing(a))
        else:
            print("Please check your spelling and try again...")
        

modularCalculator()