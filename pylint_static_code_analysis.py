# pylint_static_code_analysis

# Install pylint package 

# Run Static Code Analysis on a python program 

# Check the compliance score of a python program. 

# Fix common mistakes and improve the compliance score.

# Install pylint
# in terminal: 
# pip3 install pylint==2.11.1

# Add some code to analyze
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

# Initialize the variable 'num1' with the value 4.
num1 = 4

# Initialize the variable 'num2' with the value 5.
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))

# In Terminal:
#  pylint sample1.py

# FIX THE ERROR MESSAGES

