"""
1. Integer (int):
    Represents whole numbers, both positive and negative.
    Example: x = 42

2. Floating-Point (float):
    Represents decimal numbers (floating-point numbers).
    Example: pi = 3.14

3. String (str):
    Represents a sequence of characters enclosed in single, double, or triple quotes.
    Example: name = "Alice"

4. Boolean (bool):
    Represents a binary value, either True or False.
    Example: is_student = True

5. List:
    Represents an ordered, mutable collection of items enclosed in square brackets.
    Example: fruits = ["apple", "banana", "cherry"]

6. Tuple:
    Represents an ordered, immutable collection of items enclosed in parentheses.
    Example: coordinates = (5, 3)

7. Set:
    Represents an unordered collection of unique elements enclosed in curly braces.
    Example: colors = {"red", "green", "blue"}

8. Dictionary (dict):
    Represents a collection of key-value pairs enclosed in curly braces.
    Example: person = {"name": "John", "age": 30}

9. NoneType (None):
    Represents the absence of a value or a null value.
    Example: result = None

10. Complex (complex):
    Represents complex numbers with a real and imaginary part.
    Example: z = 3 + 2j

11. Bytes and Byte Arrays (bytes, bytearray):
    Represents sequences of bytes (immutable and mutable, respectively), commonly used for binary data.
    Example: data = b'Hello' or byte_array = bytearray([72, 101, 108, 108, 111])

12. Range (range):
    Represents an immutable sequence of numbers, often used for looping.
    Example: my_range = range(1, 6) (Generates numbers 1 to 5)

"""

#Examples of data types

#Integer(int)
x = 42

#Floating point(float)
pi = 3.14

#String(str)
name = "Alice"

#Boolean(bool)
is_student = True

#List
fruits = ["apple", "banana", "cherry"]

#Tuple
coordinates = (5, 3)

#Set
colors = {"red", "green", "blue"}

#Dictonary(dict)
person = {"name": "John", "age": 30}

#NoneType(None)
result = None

#Commplex(complex)
z = 3 + 2j

#Bytes and byte arrays (bytes, bytearray):
data = b'Hello'
byte_array = bytearray([72, 101, 108, 108, 111])

#Range(range):
my_range = range(1, 6)



#Operations---------------------------------

#Integer(int)
#arithmetic operations: +, -, *, /, // (integer division), % (modulo)
x = 42
y = 10
result = x + y  # Addition

#Floating point(float)
#Arithmetic operations: +, -, *, /
pi = 3.14
radius = 2.0
area = pi * (radius ** 2)  # Calculation of circle area

#String(str)
#concatenation: +
#indexing and slicing
name = "Alice"
greeting = "Hello, " + name
first_letter = name[0]  # Accessing the first character

#Boolean(bool)
#logical operations: and, or, not
#comparison operators: == (equal), != (not equal), <, >, <=, >=
is_student = True
is_adult = not is_student
age = 20
is_old_enough = age >= 18

#List
#indexing and slicing
#list methods: append(), remove(), pop(), extend(), etc.
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
fruits.append("orange")

#Tuple
#indexing and slicing
#Since tuples are immutable, you can't modify their elements once defined.
coordinates = (5, 3)
x_coord = coordinates[0]
example = (5, 3, 6, 8)

#Set
#set operations: union(), intersection(), difference(), add(), remove(), etc.
colors = {"red", "green", "blue"}
colors.add("yellow")

#Dictonary(dict)
#accessing values using keys
#dictionary methods: keys(), values(), items(), get(), pop(), etc.
person = {"name": "John", "age": 30}
person_name = person["name"]

#NoneType(None)
#typically used to represent the absence of a value.
result = None

#Commplex(complex)
#arithmetic operations: +, -, *, /
z1 = 3 + 2j
z2 = 1 - 1j
z_sum = z1 + z2

#Bytes and byte arrays (bytes, bytearray):
#indexing and slicing (similar to strings)
data = b'Hello'
first_byte = data[0]

#Range(range):
#Typically used for looping and iterating over a sequence of numbers.
my_range = range(1, 6)  # Represents numbers 1 to 5
for num in my_range:
    print(num)



#Type casting------------------------------------
num_str = "42"
num_int = int(num_str)  # Converts the string "42" to an integer

num_str = "3.14"
num_float = float(num_str)  # Converts the string "3.14" to a float

num = 42
num_str = str(num)  # Converts the integer 42 to a string "42"

value = 0
value_bool = bool(value)  # Converts 0 to False

value = "Hello"
list_value = list(value)   # Converts the string "Hello" to a list ["H", "e", "l", "l", "o"]
tuple_value = tuple(value)  # Converts to a tuple ("H", "e", "l", "l", "o")
set_value = set(value)      # Converts to a set {"H", "e", "l", "o"}

char = 'A'
ascii_value = ord(char)   # Converts 'A' to its ASCII value (65)
char_again = chr(65)     # Converts 65 back to the character 'A'

num = 255
hex_value = hex(num)  # Converts 255 to '0xff' (hexadecimal)
oct_value = oct(num)  # Converts 255 to '0o377' (octal)
