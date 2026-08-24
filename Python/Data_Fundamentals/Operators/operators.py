# Acutis_Codes/Python/Data_Fundamentals/Operators/operators.py

"""
    Operators are used to perform operations on variables and values
    They are one of 4 built-in data types in Python used to store collections of data
    The other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

    Operators are used to perform operations on variables and values
    Examples of operators include:
    1. Arithmetic operators: +, -, *, /, %, **, //
    2. Comparison operators: ==, !=, >, <, >=, <=
    3. Logical operators: and, or, not
    4. Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
    5. Bitwise operators: &, |, ^, ~, <<, >>
    6. Membership operators: in, not in
    7. Identity operators: is, is not

    NB: Operator precedence: The order in which operators are evaluated in an expression 

"""

# Implementation of operators in python
# Arithmetic operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Comparison operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal To:", a >= b)
print("Less Than or Equal To:", a <= b)

# Logical operators
print("Logical AND:", a > 5 and b < 10)
print("Logical OR:", a > 5 or b < 10)
print("Logical NOT:", not(a > 5))

# Assignment operators
c = 10
print("Assignment:", c)
c += 5
print("Addition Assignment:", c)
c -= 5
print("Subtraction Assignment:", c)
c *= 5
print("Multiplication Assignment:", c)
c /= 5
print("Division Assignment:", c)
c %= 5
print("Modulus Assignment:", c)
c **= 5
print("Exponentiation Assignment:", c)
c //= 5
print("Floor Division Assignment:", c)

# Bitwise operators
d = 10
e = 5
print("Bitwise AND:", d & e)
print("Bitwise OR:", d | e)
print("Bitwise XOR:", d ^ e)
print("Bitwise NOT:", ~d)
print("Left Shift:", d << 2)
print("Right Shift:", d >> 2)

# Membership operators
myList = [1, 2, 3, 4, 5]

print("Membership IN:", 3 in myList)
print("Membership NOT IN:", 6 not in myList)

# Identity operators
f = 10
g = 10
print("Identity IS:", f is g)
print("Identity IS NOT:", f is not g)

# Operator precedence
x = 10 + 5 * 2
print("Operator Precedence:", x)


