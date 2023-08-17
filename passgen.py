# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:38:38 2023

@author: Shafeeq
"""

import string





def generate_password(length):
    #defining all uppercase & lowercase, digit and punctuations
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #to create the password, import random letters,digit and punctuations and return it 
    password = ''.join(__import__('random').choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator!")
    
    # Enter your name
    user_name = input("Enter username: ")
    print(f"Hello, {user_name}!")
    
    
    try:
        length = int(input("Enter password length: "))
        
        #if length is a negative integer, print Error
        if length <= 0:
            print("Error! Please enter a positive integer.")
            return
        
        #if there is value error, other than positive integer or negative integrer
    except ValueError:
        print("Error! Invalid value. Enter a valid number.")
        return
    
    #if there are no such errors pass the random values created before to the length desired and print it.
    password = generate_password(length)
    
    print("Password Generated is :", password)

if __name__ == "__main__":
    main()