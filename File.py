#Opening a File:

#file = open('filename', 'mode')

"""
'filename' is the name of the file you want to open.
'mode' is a string that specifies the file access mode:
'r': Read (default mode)
'w': Write (creates a new file or truncates an existing file)
'a': Append (opens the file for writing, but doesn't truncate it)
'b': Binary mode (e.g., 'rb' for reading binary files)
"""

#Reading from a File:----------------------------
# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace


#Writing to a File:-----------------------------
# Writing data to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test.\n")

# Appending data to a file
with open('example.txt', 'a') as file:
    file.write("Appending additional data.\n")

#Closing a File:-------------------------------
file = open('example.txt', 'r')
# File operations here
file.close()  # Don't forget to close the file

# Using the with statement (recommended)
with open('example.txt', 'r') as file:
    # File operations here
# File is automatically closed when the block is exited

#Checking if a File Exists:--------------------
    import os

if os.path.exists('example.txt'):
    print("The file exists.")
else:
    print("The file does not exist.")

