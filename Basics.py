#variables-------------------------------

# Integer variable
age = 30

# String variable
name = "John Doe"

# Float variable
salary = 45000.50

# Boolean variable
is_student = True

#division--------------------------------

# Input integers
dividend = 20
divisor = 3

# Perform division and get quotient
quotient = dividend // divisor  # Using integer division (//) to get the quotient

# Calculate the dividend
remainder = dividend % divisor  # Using the modulo operator (%) to get the remainder

#string_operations-----------------------

my_string = "Hello, World!"
length = len(my_string)  # 13
substring = my_string[7:12]  # "World"
character = substring[2] # "r"

#print_operations------------------------

#Printing text
print("Hello, World!")  # Prints the text "Hello, World!"

#Printing variables
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)

#Concatenating strings
name = "Bob"
age = 25
print("Name:", name, "Age:", age)

#Formatting output:
name = "Charlie"
age = 35
print(f"Name: {name}, Age: {age}")

name = "David"
age = 40
print("Name: {}, Age: {}".format(name, age))

#Printing multiple lines
print("Line 1")
print("Line 2")

#Printing with line breaks
print("Hello", end=" ") #this end="" is stopping the line form ending
print("World!")


#User input-----------------------------------------
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Display a greeting using the user's input


#Arithmatic operations------------------------------

#addition
result = 5 + 3  # result is 8

#substraction
result = 10 - 4  # result is 6

#multiplication
result = 6 * 7  # result is 42

#dividion
result = 15 / 3  # result is 5.0

#integer division
result = 17 // 3  # result is 5

#modulo(%)
result = 17 % 3  # result is 2

#exponentiation
result = 2 ** 3  # result is 8
pow(2,3) # result is 8

#negation
x = 5
neg_x = -x  # neg_x is -5

#Absolute Value
x = -7
abs_x = abs(x)  # abs_x is 7

#combining
result = (3 + 2) * 4  # result is 20
