# Python/Data_Fundamentals/Variables_&_DataTypes/datatypes.py
#
# VARIABLES & DATA TYPES
#
# A variable is just a name that points to a value stored in memory.
# Python figures out the type of that value automatically -- you never
# have to declare "this is an integer" like you would in some other
# languages. This file walks through Python's core built-in types.


# ---------------------------------------------------------------------------
# 1. int -- whole numbers, positive or negative, no decimal point
# ---------------------------------------------------------------------------
age = 25
temperature_below_zero = -10

print("age:", age, "| type:", type(age))
print("temperature_below_zero:", temperature_below_zero, "| type:", type(temperature_below_zero))

# Python ints have no size limit (unlike many languages, where an int
# overflows past a fixed number of bits). This will work fine:
big_number = 10 ** 30
print("big_number:", big_number, "| type:", type(big_number))


# ---------------------------------------------------------------------------
# 2. float -- numbers with a decimal point
# ---------------------------------------------------------------------------
price = 19.99
pi_estimate = 3.14159

print("\nprice:", price, "| type:", type(price))
print("pi_estimate:", pi_estimate, "| type:", type(pi_estimate))

# Careful: floats are stored in binary, so some "simple" decimal math
# doesn't come out exactly even. This is normal, not a bug in Python.
print("0.1 + 0.2 =", 0.1 + 0.2)  # not exactly 0.3 -- try it yourself


# ---------------------------------------------------------------------------
# 3. str -- text, wrapped in single or double quotes (both work the same)
# ---------------------------------------------------------------------------
first_name = "Ada"
last_name = 'Lovelace'

print("\nfirst_name:", first_name, "| type:", type(first_name))

# Strings can be combined ("concatenated") with +
full_name = first_name + " " + last_name
print("full_name:", full_name)

# Or formatted with an f-string -- the modern, preferred way in Python
greeting = f"Hello, {full_name}!"
print("greeting:", greeting)

# Strings are sequences, so you can index and slice them like a list
print("first letter:", full_name[0])
print("first three letters:", full_name[0:3])


# ---------------------------------------------------------------------------
# 4. bool -- True or False (note the capital letters, that's required)
# ---------------------------------------------------------------------------
is_logged_in = True
has_permission = False

print("\nis_logged_in:", is_logged_in, "| type:", type(is_logged_in))

# Booleans are actually a subtype of int under the hood: True == 1, False == 0
print("True + True =", True + True)      # 2
print("True == 1:", True == 1)           # True


# ---------------------------------------------------------------------------
# 5. NoneType -- represents "no value" or "nothing here yet"
# ---------------------------------------------------------------------------
current_user = None
print("\ncurrent_user:", current_user, "| type:", type(current_user))

# None is not the same as 0, "", or False -- it specifically means
# "this variable has no value assigned to it."
print("None == False:", None == False)   # False -- they are NOT the same


# ---------------------------------------------------------------------------
# 6. Converting between types ("type casting")
# ---------------------------------------------------------------------------
# Python is strongly typed -- it won't silently mix types for you.
# You have to convert explicitly using int(), float(), str(), bool().

age_as_text = "25"
age_as_number = int(age_as_text)
print("\nage_as_text:", age_as_text, "| type:", type(age_as_text))
print("age_as_number:", age_as_number, "| type:", type(age_as_number))

# This works because "25" only contains digits.
# This would NOT work -- uncomment to see the error for yourself:
# broken = int("twenty five")   # ValueError: invalid literal for int()

# float -> int truncates (cuts off) the decimal part, it does not round
print("int(9.9) =", int(9.9))   # 9, not 10

# Almost anything can be converted to a string
print("str(42):", str(42), "| type:", type(str(42)))

# bool() follows a simple rule: 0, empty values, and None are False.
# Everything else is True.
print("\nbool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(""))
print("bool('hello'):", bool("hello"))
print("bool(None):", bool(None))
print("bool([]):", bool([]))       # empty list -- False
print("bool([1, 2]):", bool([1, 2]))  # non-empty list -- True


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Create a variable of each type covered above with your own values.
# 2. Predict what type(x) will print for each one, then check yourself.
# 3. Try int("hello") and read the error message Python gives you --
#    this is what "strongly typed" means in practice, and it's the
#    exact topic covered next in Type_Systems/typesSystem.py.