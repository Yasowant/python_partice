# Data Types in Python: Number Object/Number Data Types
import math
import random
from decimal import Decimal
from fractions import Fraction

# Basic Number Operations
x = 2
y = x
print(x)  # Output: 2
print(y)  # Output: 2
x = 15
print(x)  # Output: 15
print(y)  # Output: 2

# Arithmetic Operations
a, b, c = 2, 4, 5
print(a + b)         # Output: 6
print(40 + 2.3)      # Output: 42.3
print(int(2.3))      # Output: 2
print(float(40))     # Output: 40.0
print(8 + float(67)) # Output: 75.0
print("Yasowant" + " Nayak")  # Output: Yasowant Nayak

# Printing variables
print(x, y, c)       # Output: 15 2 5
print(x + 1, y * 2)  # Output: 16 4

# Modulo, Exponentiation, Comparisons
print(c % 2)         # Output: 1
print(b ** 3)        # Output: 64
print(1 < 2)         # Output: True
print(5 == 5.0)      # Output: True
print(1 == 2 and 2 < 3)  # Output: False

# Using math module
print(math.floor(3.5))   # Output: 3
print(math.floor(-3.5))  # Output: -4
print(math.trunc(2.6))   # Output: 2
print(math.trunc(-2.8))  # Output: -2

# Complex Numbers
print((6 + 5j) * 5)  # Output: (30+25j)

# Octal and Hexadecimal Numbers
print(oct(54))       # Output: 0o66
print(hex(64))       # Output: 0x40
print(int('64', 8))  # Output: 52

# Random Module Usage
print(random.random())        # Output: Random float between 0.0 and 1.0
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
l1 = ["Yasowant", "Mayank", "Disney", "Zahira"]
print(random.choice(l1))      # Output: Random choice from the list
random.shuffle(l1)            # Shuffles the list in-place
print(l1)                     # Output: Shuffled list

# Decimal and Fraction types (Additional Number Types)
d1 = Decimal('10.5')
d2 = Decimal('2.1')
print(d1 + d2)  # Output: 12.6 (precise addition)

f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 + f2)  # Output: 11/15

# Set Operations: Union and Intersection
set1 = {1, 2, 3, 4}
set2 = {1, 3}
print(set1 | set2)  # Union: {1, 2, 3, 4}
print(set1 & set2)  # Intersection: {1, 3}
print(set1 - set2)  # Difference: {2, 4}
print(set1 ^ set2)  # Symmetric Difference: {2, 4}
