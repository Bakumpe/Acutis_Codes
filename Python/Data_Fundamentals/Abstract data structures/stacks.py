# Acutis_codes/Python/Data_Fundamentals/Abstract data structures/stacks.py

"""
    Stacks are used to store multiple items in a single variable
    They are one of 4 built-in data types in Python used to store collections of data

    Stacks are a linear data structure that follows the Last In First Out (LIFO) principle
    The last element added to the stack will be the first one to be removed    

"""

# Initiating an empty stack
myStack = []

myStack.append(1)
myStack.append("Hello")
myStack.append(3)

print(myStack)
myStack.pop() # Removes the last element from the stack
print(myStack)