# This program shows how to use modules in Python.

# A module is like a toolbox. It contains ready-made tools (code) that we can use.
# For example, the "math" module has many math functions like square root, pi, etc.

# Step 1: Import the module we want to use
import math

# Now we can use functions from the math module.
# Let's use math.sqrt() to find the square root of a number

number = 25  # This is the number we want the square root of

# Step 2: Use the sqrt() function from the math module
square_root = math.sqrt(number)

# Step 3: Print the result
print("The square root of", number, "is", square_root)

# You can also use other functions like math.pi to get the value of pi
print("The value of pi is:", math.pi)

# Summary:
# - We imported the math module using 'import math'
# - Then used math.sqrt() and math.pi
# - Modules save time by giving us useful code so we don’t have to write everything ourselves!
