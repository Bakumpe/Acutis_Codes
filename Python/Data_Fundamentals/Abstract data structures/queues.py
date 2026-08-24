# Acutis_Codes/Python/Data_Fundamentals/Abstract data structures/queues.py

"""
    Queues are used to store multiple items in a single variable
    They are one of 4 built-in data types in Python used to store collections of data

    Queues are a linear data structure that follows the First In First Out (FIFO) principle
    The first element added to the queue will be the first one to be removed    

"""
# Initiating an empty queue
myQueue = []

myQueue.append(1)
myQueue.append("Hello")
myQueue.append(3)

print(myQueue) 

myQueue.pop(0) # Removes the first element from the queue
print(myQueue)

"""
    Using deque from the collections module to implement a queue
    Deque is a double-ended queue that allows you to add and remove elements from both ends

    Deque is more efficient than using a list for implementing a queue because it has O(1) 
    time complexity for adding and removing elements from both ends, while a list has O(n) 
    time complexity for removing elements from the front of the list.

"""
from collections import deque

myQueue = deque()
myQueue.append(1)
myQueue.append("Hello")
myQueue.append(3)

print(myQueue)

myQueue.popleft() # Removes the first element from the queue
print(myQueue)