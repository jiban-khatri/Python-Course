# ============================================================
# NUMBERS IN PYTHON - COMPLETE GUIDE (WITH COMMENTS)
# ============================================================

# In Python, numbers are mainly of 3 types:
# 1. int   -> Integer numbers (whole numbers)
# 2. float -> Decimal numbers
# 3. complex -> Numbers with imaginary parts

# ------------------------------------------------------------
# 1. INTEGER (int)
# ------------------------------------------------------------

# Integers are whole numbers without decimals

a = 10
b = -5
c = 0

print(a)  # 10
print(type(a))  # <class 'int'>



# ------------------------------------------------------------
# 2. FLOAT (decimal numbers)
# ------------------------------------------------------------

# Floats are numbers with decimal points

x = 3.14
y = -2.5
z = 0.0

print(x)  # 3.14
print(type(x))  # <class 'float'>



# ------------------------------------------------------------
# 3. COMPLEX NUMBERS
# ------------------------------------------------------------

# Complex numbers have a real part and imaginary part
# Format: a + bj

num = 3 + 4j

print(num)  # (3+4j)
print(type(num))  # <class 'complex'>



# ------------------------------------------------------------
# TYPE CONVERSION
# ------------------------------------------------------------

# Convert between number types

a = 10

# int to float
b = float(a)
print(b)  # 10.0

# float to int
c = int(5.8)
print(c)  # 5

# int to complex
d = complex(5)
print(d)  # (5+0j)



# ------------------------------------------------------------
# BASIC MATHEMATICAL OPERATIONS
# ------------------------------------------------------------

a = 10
b = 3

# Addition
print(a + b)  # 13

# Subtraction
print(a - b)  # 7

# Multiplication
print(a * b)  # 30

# Division (always returns float)
print(a / b)  # 3.3333...

# Floor Division (removes decimal)
print(a // b)  # 3

# Modulus (remainder)
print(a % b)  # 1

# Power (exponent)
print(a ** b)  # 1000



# ------------------------------------------------------------
# ABSOLUTE VALUE
# ------------------------------------------------------------

# abs() returns positive value

print(abs(-20))  # 20



# ------------------------------------------------------------
# ROUNDING NUMBERS
# ------------------------------------------------------------

# round() rounds a float

num = 3.5678

print(round(num))      # 4
print(round(num, 2))   # 3.57



# ------------------------------------------------------------
# MAX AND MIN
# ------------------------------------------------------------

print(max(5, 10, 20, 3))  # 20
print(min(5, 10, 20, 3))  # 3



# ------------------------------------------------------------
# RANDOM NUMBERS
# ------------------------------------------------------------

# Python has a module called random

import random

# random number between 0 and 1
print(random.random())

# random integer between range
print(random.randint(1, 10))



# ------------------------------------------------------------
# MATHEMATICAL FUNCTIONS
# ------------------------------------------------------------

# Python has a math module for advanced math

import math

# square root
print(math.sqrt(16))  # 4

# power
print(math.pow(2, 3))  # 8

# value of pi
print(math.pi)

# ceiling (round up)
print(math.ceil(4.2))  # 5

# floor (round down)
print(math.floor(4.8))  # 4



# ------------------------------------------------------------
# NUMBER FORMATTING
# ------------------------------------------------------------

# limit decimal places using f-string

pi = 3.1415926535

print(f"{pi:.2f}")  # 3.14
print(f"{pi:.4f}")  # 3.1416



# ------------------------------------------------------------
# CHECK NUMBER TYPE
# ------------------------------------------------------------

a = 10
b = 3.5

print(isinstance(a, int))   # True
print(isinstance(b, float)) # True



# ------------------------------------------------------------
# LARGE NUMBERS
# ------------------------------------------------------------

# Python supports very large integers automatically

big = 999999999999999999999999999999999999
print(big)



# ------------------------------------------------------------
# NUMBER SYSTEMS
# ------------------------------------------------------------

# Binary (base 2)
binary_num = 0b1010
print(binary_num)  # 10

# Octal (base 8)
octal_num = 0o12
print(octal_num)  # 10

# Hexadecimal (base 16)
hex_num = 0xA
print(hex_num)  # 10



# Convert numbers to other bases

n = 10

print(bin(n))  # binary
print(oct(n))  # octal
print(hex(n))  # hexadecimal

