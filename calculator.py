# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:21:29 2023

@author: Shafeeq
"""
#defining the functions
def add(x, y):                           
    return x + y

def subtract(x, y):                      
    return x - y

def multiply(x, y):                     
    return x * y

def divide(x, y):                        
    if y == 0:
        return "Error! (Zero in denominator)"
    else:
        return x / y

#inputs

number1 = float(input("Enter 1st number: "))                 
number2 = float(input("Enter 2nd number: "))

#operation choice

print("Select operation: ")                        
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

#cases
case = input("Enter the operation to be performed (1/2/3/4): ")                 

#mathematical operations performed

if case == '1':
    print(number1, "+", number2, "=", add(number1, number2))
elif case == '2':
    print(number1, "-", number2, "=", subtract(number1, number2))
elif case == '3':
    print(number1, "*", number2, "=", multiply(number1, number2))
elif case == '4':
    print(number1, "/", number2, "=", divide(number1, number2))
else:
    print("Invalid Input (other than integer)")
