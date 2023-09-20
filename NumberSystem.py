#Decimal Numbers (Base 10):
decimal_num = 42

#Binary Numbers (Base 2):
binary_num = 0b1010  # Binary representation of 10

#Octal Numbers (Base 8):
octal_num = 0o52  # Octal representation of 42

#Hexadecimal Numbers (Base 16):
hexadecimal_num = 0x2A  # Hexadecimal representation of 42

#Converting Between Number Systems:
decimal_num = 42
binary_representation = bin(decimal_num)  # '0b101010'
octal_representation = oct(decimal_num)  # '0o52'
hexadecimal_representation = hex(decimal_num)  # '0x2a'

#String Formatting:
decimal_num = 42
binary_str = format(decimal_num, 'b')  # '101010'
octal_str = format(decimal_num, 'o')  # '52'
hexadecimal_str = format(decimal_num, 'x')  # '2a'

#Arithmetic Operations:
binary_num1 = 0b1010
binary_num2 = 0b1100
result = binary_num1 + binary_num2  # Decimal result: 24

#---------------------------------------------
#converting binary to Unicode haracter
# Define an 8-bit binary number as a string
binary_number = "01001001"

# Convert the binary number to an integer
decimal_number = int(binary_number, 2)

# Convert the integer to a character using the chr() function
character = chr(decimal_number)

# Print the character
print("Character:", character)

#Character to string----------------------------
# Input character
character = 'A'

# Get the Unicode code point of the character
code_point = ord(character)

# Convert the code point to a binary string and remove the '0b' prefix
binary_string = bin(code_point)[2:]

# Ensure that the binary string is 8 bits long by adding leading zeros if needed
binary_string = binary_string.zfill(8)

# Print the binary string
print("Binary String:", binary_string)
