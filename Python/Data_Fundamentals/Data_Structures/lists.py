# This is a file that explains lists in python
# Lists are used to store multiple items in a single variable
# They are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

"""
Usage:
        # 1. Lists are created using square brackets []
        # 2. Lists can contain items of different data types
        # 3. Lists are mutable, meaning that their elements can be changed after they are created
        # 4. Lists can be nested, meaning that they can contain other lists as elements
        # 5. Lists can be iterated over using loops
        # 6. Lists can be sliced, meaning that a portion of the list can be extracted
        # 7. Lists can be concatenated, meaning that two or more lists can be combined into a single list
        # 8. Lists can be repeated, meaning that a list can be multiplied by an integer to create a new list with repeated elements
        # 9. Lists can be sorted, meaning that the elements of the list can be arranged in a specific order
        # 10. Lists can be searched, meaning that the elements of the list can be checked for the presence of a specific value
        # 11. Lists can be filtered, meaning that a new list can be created containing only the elements that meet a specific condition
        # 12. Lists can be mapped, meaning that a new list can be created by applying a specific function to each element of the original list
        # 13. Lists can be reduced, meaning that a single value can be derived from
        # 14. Lists can be used to implement stacks and queues, which are data structures that allow for the efficient addition and removal of elements

Use Cases:
        # 1. Lists are used to store multiple items in a single variable
        # 2. Lists are used to store items of different data types
        # 3. Lists are used to store items that can be changed after they are created
        # 4. Lists are used to store items that can be nested
        # 5. Lists are used to store items that can be iterated over using loops
        # 6. Lists are used to store items that can be sliced
        # 7. Lists are used to store items that can be concatenated
        # 8. Lists are used to store items that can be repeated
        # 9. Lists are used to store items that can be sorted
 """

separator = "-" * 70
spaces = " " * 10


# Implementation of lists in python
# Initializing an empty list
myEmptyList = []

# Lists can contain items of different data types
myMixedList = [1, "Hello", 3.14, True]

# Lists can be nested, meaning that they can contain other lists as elements
myNestedList = [1, 2, [3, 4], 5]

# Lists can be iterated over using loops
print(separator)
for item in myMixedList:
    print(item)

# Lists can be sliced, meaning that a portion of the list can be extracted
print(myMixedList[1:3])
print(spaces)
print(separator)
# Lists can be concatenated, meaning that two or more lists can be combined into a single list
myList1 = [1, 2, 3]
myList2 = [4, 5, 6]

myConcatenatedList = myList1 + myList2
myConcatenatedList.append(7)
myConcatenatedList.extend([8, 9, 10])
myConcatenatedList.insert(0, 0)
myConcatenatedList.remove(5)
myConcatenatedList.pop()
myConcatenatedList.sort()
myConcatenatedList.reverse()

print(myConcatenatedList)
