#conditionals--------------------------------

#if Statement:
age = 25
if age >= 18:
    print("You are an adult.")

#elif Statement:
score = 85
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

#else Statement:
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Nested Conditionals:
x = 10
y = 5
if x > 5:
    if y > 3:
        print("Both conditions are met.")

#Multiple Conditions (Logical Operators):
#You can combine conditions using logical operators like and, or, and not.
age = 25
if age >= 18 and age <= 65:
    print("You are eligible to vote and work.")

#Ternary Conditional Expression:
age = 22
status = "Adult" if age >= 18 else "Minor"

#Pass Statement:
x = 10
if x > 5:
    pass  # Placeholder for future code


#Loops--------------------------------------------------
#for
#for variable in sequence:
    # Code to be repeated

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1, 6):  # Generates numbers 1 to 5
    print(i)

#while
#while condition:
    # Code to be repeated

count = 0
while count < 5:
    print(count)
    count += 1

user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print("You entered:", user_input)

#loop control
#break: Terminates the loop prematurely when a certain condition is met.
for i in range(10):
    if i == 5:
        break
    print(i)

#continue: Skips the current iteration and moves to the next one.
for i in range(5):
    if i == 2:
        continue
    print(i)

#else block is executed when the loop completes normally (i.e., without encountering a break statement).
for i in range(5):
    print(i)
else:
    print("Loop finished without a break")



#Functions----------------------------------------------
#def function_name(parameters):
    # Function body
    # Code to perform a task
    # Optional return statement

def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")

# Function call
greet("Alice")  # Output: Hello, Alice!

#Return statement:
def add(x, y):
    """This function adds two numbers."""
    result = x + y
    return result

sum_result = add(3, 5)
print(sum_result)  # Output: 8

#Default parameters
def greet(name="Guest"):
    """This function greets the person with an optional name."""
    print("Hello, " + name + "!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

#Variable-Length Argument Lists:
#Functions can accept a variable number of arguments using *args (for non-keyword arguments) and **kwargs (for keyword arguments).

def multi_add(*args):
    """This function adds all the numbers passed as arguments."""
    result = 0
    for num in args:
        result += num
    return result

sum_result = multi_add(1, 2, 3, 4)
print(sum_result)  # Output: 10

#Lambda Functions:
#here lambda is a keyword

double = lambda x: x * 2
print(double(5))  # Output: 10


#Simulating switch with functions and if elif------------------------

def switch_case(option):
    if option == "A":
        print("Option A selected")
    elif option == "B":
        print("Option B selected")
    elif option == "C":
        print("Option C selected")
    else:
        print("Invalid option")

# Usage
choice = "B"
switch_case(choice)
