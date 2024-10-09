# Notes from Python for Data Science, AI and Development

# Check the Python Version
import sys
print(sys.version)


# System settings about float type
import sys
sys.float_info

# Convert 2 to a float
float(2)

# Convert integer 2 to a float and check its type
type(float(2))

# Convert a string into an integer
int('1')

# Convert an integer to a string
str(1)

# Type of True
type(True)

#We can cast boolean objects to other data types. If we cast a boolean with a value of True to an integer or float we will get a one. 
# If we cast a boolean with a value of False to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a True. 

# Convert 1 to boolean
bool(1)

# Convert 0 to boolean
bool(0)

# Write the code to convert this phone number 123-456-7890 to a string
type(str("123-456-7890"))

# String interpolation
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

# Raw Strings: raw strings are a powerful tool for handling textual data, especially when dealing with escape characters. 
# By prefixing a string literal with the letter ‘r’, Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences.

# You need to put an 'r' in front of regular string paths with backslashes to make it into a raw string
# This means that \n is not interpreted as a newline character, but rather as two separate characters, ‘’ and ‘n’. Consequently, the file path is represented exactly as it appears.
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
# Output: 
Raw String: C:\new_folder\file.txt

# Assign string to variable
name = "Michael Jackson"
name

# Print the first element in the string

print(name[0])


# Print the element on index 6 in the string

print(name[6])

# Lists have []-------------------------------------------------------------

# Append one element
fruits = ["apple", "banana", "orange"] 
fruits.append("mango") print(fruits)

# Copy a list
my_list = [1, 2, 3, 4, 5] 
new_list = my_list.copy() print(new_list) 
# Output: [1, 2, 3, 4, 5]

# Count occurances of a specific element
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2) print(count) 
# Output: 4

# Create a list
fruits = ["apple", "banana", "orange", "mango"]

# Remove a element from a specific index
my_list = [10, 20, 30, 40, 50] 
del my_list[2] # Removes the element at index 2 print(my_list) 
# Output: [10, 20, 40, 50]

# Add multiple elements to a list
fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits)

# Insert elements
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)

# Assign new values to specific elements
my_list = [10, 20, 30, 40, 50] 
my_list[1] = 25 # Modifying the second element 
print(my_list) 
# Output: [10, 25, 30, 40, 50]

# Remove and return an element at a specific index OR the last element by default if you don't specify an index
my_list = [10, 20, 30, 40, 50] 
removed_element = my_list.pop() # Removes and returns the last element 
print(removed_element) 
# Output: 50 

print(my_list) 
# Output: [10, 20, 30, 40]

# Remove the first occurance of a specified value
my_list = [10, 20, 30, 40, 50] 
my_list.remove(30) # Removes the element 30 
print(my_list) 
# Output: [10, 20, 40, 50]

# Reverse the order of the elements in a list
my_list = [1, 2, 3, 4, 5] 
my_list.reverse() print(my_list) 
# Output: [5, 4, 3, 2, 1]

# Access a range of elements in list with slicing
my_list = [1, 2, 3, 4, 5] 
print(my_list[1:4]) 
# Output: [2, 3, 4] (elements from index 1 to 3)

print(my_list[:3]) 
# Output: [1, 2, 3] (elements from the beginning up to index 2) 

print(my_list[2:]) 
# Output: [3, 4, 5] (elements from index 2 to the end) 

print(my_list[::2]) 
# Output: [1, 3, 5] (every second element)

# Sort in ascending order ( for decending add the reverse=True argument)
my_list = [5, 2, 8, 1, 9] 
my_list.sort() 
print(my_list) 
# Output: [1, 2, 5, 8, 9] 

my_list = [5, 2, 8, 1, 9] 
my_list.sort(reverse=True) 
print(my_list) 
# Output: [9, 8, 5, 2, 1]

# Tuples ============================================================================================

# Count how many times a specified element appears in the tuple
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple")) #Counts the number of times apple is found in tuple.
#Output: 2

# Find and return a value at a certain index
fruits = ("apple", "banana", "orange")
print(fruits[1]) #Returns the value at which apple is present.
#Output: banana

# Sum all elements in tuple
numbers = (10, 20, 5, 30)
print(sum(numbers))
#Output: 65

# Find min and max values
numbers = (10, 20, 5, 30)
print(min(numbers))  
#Output: 5
print(max(numbers))
#Output: 30

# Get number of elements tuple
fruits = ("apple", "banana", "orange")
print(len(fruits)) #Returns length of the tuple.
#Output: 3

# Dictionaries ==========================================================================================================

# Create a dictionary
dict_name = {} #Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}

# Access a value with its key
Value = dict_name["key_name"]

# Insert a new key/value pair, if the key already exist, it will update that key because keys have to be unique
dict_name[key] = value
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"  # Update the existing value for the same key

# Remove a specified key/vaule pair from dictionary, will raise KeyError if key does not exit
del dict_name[key]
del person["Country"]

# Merge provided dictionary into an existing dictionary, either adding or updating key-value pairs
dict_name.update({key: value})
person.update({"Profession": "Doctor"})

# Clear or delete all key/value pairs in a dictionary
dict_name.clear()
grades.clear()

# Check for the existence of a key in a dictionary
if "name" in person:
    print("Name exists in the dictionary.")

# Create a shallow copy of the dictionary ( they will remain distinct objects in memory)
new_dict = dict_name.copy()
new_person = person.copy()
new_person = dict(person) # another way to create a copy of dictionary

# List all keys in a list ( so you can iterate over them)
keys_list = list(dict_name.keys())
person_keys = list(person.keys())

# Extract all values from dictionary and convert to a list
values_list = list(dict_name.values())
person_values = list(person.values())

# Retrieve all key/value pairs as tuples and convert them into a list of tuples ( so each tuple has a key and it's corresponding value)
items_list = list(dict_name.items())
info = list(person.items())


# Sets (like Ven Diagram)============================================================================================================
# A set is an unordered collection of unique elements. Sets are enclosed in curly braces `{}`. They are useful for storing distinct values and performing set operations.

# Add an element to a set, duplicates are automatically removed because sets only store unique values
set_name.add(element) 
fruits.add("mango")

# Clear all elements from set
set_name.clear() 
fruits.clear()

# Create a shallow copy of set. Any modifications of new copy will not affect the original set
new_set = set_name.copy() 
new_fruits = fruits.copy()

# Delete or discard a specific element from set, will ignore it if element does not exist
set_name.discard(element) 
fruits.discard("apple")

# Check if a current set is a subset of another set. Will return True if all elements of current sets are present in the other set, otherwise False. 
is_subset = set1.issubset(set2)
is_subset = fruits.issubset(colors)

# Remove and return an arbitrary element from the set. Will give KeyError if set empty. Only use when order does not matter .
removed_element = set_name.pop() 
removed_fruit = fruits.pop()

# Remove a specific element from set. Will raise KeyError of element not found.
set_name.remove(element) 
fruits.remove("banana")

# Perform operations on set such as: union, intersection, difference, symmetric difference
union_set = set1.union(set2) 
intersection_set = set1.intersection(set2) 
difference_set = set1.difference(set2) 
sym_diff_set = set1.symmetric_difference(set2) 

combined = fruits.union(colors) 
common = fruits.intersection(colors) 
unique_to_fruits = fruits.difference(colors) 
sym_diff = fruits.symmetric_difference(colors)

# Add elements from another iterable ( like a list) into the set
set_name.update(iterable) 
fruits.update(["kiwi", "grape"])

# Check if  two values are equal with equality operator
age = 25
if age == 25:
    print("You are 25 years old.")

# Check if two values are not equal with inequality operator
if age != 30:
    print("You are not 30 years old.")

# Compare if one value is greater than another
if age>= 20:
    print("Yes, the Age is greater than 20")

# Do an if statement
age = 20
if age >= 21:
    print("You can enter the bar.")
else:
    print("Sorry, you cannot enter.")

# Do elif statement for mulitple conditions
if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry, you cannot do either.")

# atm if else statement example
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = input("Enter the amount to withdraw: ")
    if amount % 10 == 0:
        dispense_cash(amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")

# Logical Operators

# NOT operator
is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received")

# AND operator
has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door()

# OR operator
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    choose a movie()

# For loops
# For Loops: Use for loops when you know the number of iterations in advance and want to process each element in a sequence. They are best suited for iterating over collections and sequences where the length is known.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# Using a range based loop to count how many steps it takes to get to a certain goal
for number in range(1, 11):
    print(number)

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# If given one argument (e.g., range(11)), it generates a sequence starting from 0 up to (but not including) the given number.
for number in range(11):
    print(number)
#If given two arguments (e.g., range(1, 11)), it generates a sequence starting from the first argument up to (but not including) the second argument.
for number in range(1, 11):
    print(number)

# Enumerated Loop: Have you ever needed to keep track of both the item and its position in a list? An enumerated for loop comes to your rescue. It's like having a personal assistant who not only hands you the item but also tells you where to find it.
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

# While Loops
# it repeats a task as long as a certain condition is true. It's like saying, "Hey computer, keep doing this until I say stop!"
# use a while loop to count from 1 to 10
# Use while loops when you need to perform a task repeatedly as long as a certain condition holds true.
# While loops are particularly useful for situations where the number of iterations is uncertain or where you're waiting for a specific condition to be met.
count = 1
while count <= 10:
    print(count)
    count += 1


#Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


# *** Python Functions ======================================================================

def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12

# Built in functions

# Calculate length of a sequence or list or string
string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])   # Output: 5

# Add elements in a list or tuple
total = sum([10, 20, 30, 40, 50])  # Output: 150

# Return max value in an iterable like a list, tuple, etc
highest = max([5, 12, 8, 23, 16])  # Output: 23

# Return minimum in a list
lowest = min([5, 12, 8, 23, 16])  # Output: 5

# Using pass
# A "pass" statement in a programming function is a placeholder or a no-op (no operation) statement. Use it when you want to define a function or a code block syntactically but do not want to specify any functionality or implementation at that moment.
# No Operation: "pass" itself doesn't perform any meaningful action. When the interpreter encounters “pass”, it simply moves on to the next statement without executing any code
#Placeholder: "pass" acts as a temporary placeholder for future code that you intend to write within a function or a code block

def function_name():
    pass

# Print a greeting
def greet(name):
    print("Hello, " + name)

result = greet("Alice")
print(result)  # Output: Hello, Alice

# Docstrings (Documentation Strings)
# Docstrings explain what a function does
# Placed inside triple quotes under the function definition
# Helps other developers understand your function
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)


# Add two numbers
def add(a, b):
    return a + b

sum_result = add(3, 5)  # sum_result gets the value 8

# Global Variables
global_variable = "I'm global"

# Local variables (available only within a function)
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

# Call the function by invoking it, it will print the local and global variables
example_function()

# Print global function to prove it is available both inside and outside the function, if you tried to print the local variable
# if you tried to print the local variable it would throw a NameError
print(global_variable)  # Accessible outside the function

# Functions with loops
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)

print_numbers(5)  # Output: 1 2 3 4 5

def greet(name):
    return "Hello, " + name

for _ in range(3):
    print(greet("Alice"))

# Modifying data structures with functions

# Define an empty list as the initial data structure
my_list = []

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

# Function to remove an element from the list
# Note: this will only remove the first occurance of the element
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")


# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

# Print the current list
print("Current list:", my_list)

# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list

# Get a help on add function ( if someone wrote correct documentation within the function with the three """)

help(add)

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Use mult() multiply two different type values together

Mult(2, "Michael Jackson ")

# Function with local variable
# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output

MJ()

# See the output

MJ1()

# See what functions returns are

print(MJ())
print(MJ1())

# Define the function for combining strings

def con(a, b):
    return(a + b)

# Test on the con() function

con("This ", "is")

# If/else in a function
# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 

#You will see below will return an error as integer alone is not considered while using a function.
# Note: It either has to be in the form of tuple, list or a set.

sum(1,2)

# Define a tuple
a = (1, 2)

# Pass the tuple to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the tuple {a} is {c}.")

# Define a list
a = [1, 2]

# Pass the list to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the list {a} is {c}.")

# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])

#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")

#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")

# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input

isGoodRating()
isGoodRating(10)

# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 

artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

# Append to list
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList

# Function that divides first input by second input

def div(a, b):
    return (a/b)


# *** Dealing with Exceptions

# ZeroDivisionError: This error arises when an attempt is made to divide a number by zero. Division by zero is undefined in mathematics, causing an arithmetic error.
result = 10 / 0 
print(result)
# Raises ZeroDivisionError

# ValueError: This error occurs when an inappropriate value is used within the code. An example of this is when trying to convert a non-numeric string to an integer:
num = int("abc")
# Raises ValueError

#FileNotFoundError: This exception is encountered when an attempt is made to access a file that does not exist
with open("nonexistent_file.txt", "r") as file:
        content = file.read()   # Raises FileNotFoundError

# IndexError: An IndexError occurs when an index is used to access an element in a list that is outside the valid index range.
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError

# KeyError: The KeyError arises when an attempt is made to access a non-existent key in a dictionary.
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError

# TypeError: The TypeError occurs when an object is used in an incompatible manner. An example includes trying to concatenate a string and an integer
result = "hello" + 5   
# Raises TypeError

# AttributeError: An AttributeError occurs when an attribute or method is accessed on an object that doesn't possess that specific attribute or method
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError

# ImportError: This error is encountered when an attempt is made to import a module that is unavailable.
#  For example: import non_existent_module

# Using try/except
# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")

# Try / except block example
# potential code before try catch

try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception

# Using an incorrect input
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        

# Example specific try/exception
# potential code before try catch

try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
    
# code that will execute if there is no exception or a one that we are handling

# multiple exceptions example
# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# Using else with exceptions when you want something else to execute or print when there are no exceptions
# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

# Let user know we are done processing their input with finally
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

# dividing safely
def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator)) 

# square root exceptions
import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
# Test case
number1=float(input("Enter the number:-"))
perform_calculation(number1)

# other exception example
def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")
# Test case
user_input = float(input("Enter a number: "))
complex_calculation(user_input)


# Creating Classes in Python ==============================================================================================================

# class declaration
class ClassName:

# class attribute
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value

class ClassName:
    # Class attributes (shared by all instances)
    # Ex. for car instance
    class_attribute = value

    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...

    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ...):
        # Method logic
        pass

    def method2(self, parameter1, parameter2, ...):
        # Method logic
        pass

# Creating objects ( instances of the the class)
# Create objects (instances) of the class
# Args are attributes
object1 = ClassName(arg1, arg2, ...)
object2 = ClassName(arg1, arg2, ...)

# Calling methods on objects
# Method 1: Using dot notation
result1 = object1.method1(param1_value, param2_value, ...)
result2 = object2.method2(param1_value, param2_value, ...)

# Method 2: Assigning object methods to variables
method_reference = object1.method1  # Assign the method to a variable
result3 = method_reference(param1_value, param2_value, ...)

# Accessing object attributes
attribute_value = object1.attribute1  # Access the attribute using dot notation

# Modifying object attributes
object1.attribute2 = new_value  # Change the value of an attribute using dot notation

# Accessing class attributes (shared by all instances)
class_attr_value = ClassName.class_attribute

# Example of car class
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
    
# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

# break and continue
# `break` exits the loop prematurely. `continue` skips the rest of the current iteration and moves to the next iteration.
for: # Code to repeat 
    if # boolean statement
        break 

for: # Code to repeat  
    if # boolean statement
        continue

for num in range(1, 6):
    if num == 3:
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# range review
range(5) #generates a sequence of integers from 0 to 4. 
range(2, 10) #generates a sequence of integers from 2 to 9. 
range(1, 11, 2) #generates odd integers from 1 to 9.

# Try-Except block
# Tries to execute the code in the try block. If an exception of the specified type occurs, the code in the except block is executed.
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.")

# Try-Except with Else Block
# Code in the `else` block is executed if no exception occurs in the try block
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number") 
else: 
    print("You entered:", num)

# Try-Except with Finally Block
# C# try: # Code that might raise an exception except 
# ExceptionType: # Code to handle the exception 
# finally: # Code that always executes 

try: 
    file = open("data.txt", "r") 
    data = file.read() 
except FileNotFoundError: 
    print("File not found.") 
finally: 
    file.close()

# while loop
count = 0 while count < 5: 
    print(count) count += 1

# Module 4 - Reading files with Open ==============================================
 
# Open the file in read ('r') mode
file = open('file.txt', 'r')

# Using with statement ( best practice)
# To simplify file handling and ensure proper closure of files, Python provides the "with" statement. It automatically closes the file when operations within the indented block are completed. This is considered best practice when working with files.
# Open the file using 'with' in read ('r') mode
with open('file.txt', 'r') as file:
    # further code

# Read contents of txt file
# Reading and Storing the Entire Content of a File

# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.

# Step 1: Open the file you want to read
with open('file.txt', 'r') as file:

    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()

    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.

    # For example, let's print the content to the console:
    print(file_stuff)

# Step 4: The 'with' statement automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.

# Read file line by line
#The 'readlines' method reads the file line by line and stores each line as an element in a list. The order of lines in the list corresponds to their order in the file.

#The 'readline' method reads individual lines from the file. It can be called multiple times to read subsequent lines.

# First open file
file = open('file.txt', 'r')

# Read line by line
# readline() helps you read a text file line by line, allowing you to work with each line of text as you go. It's like taking one sentence at a time from a book and doing something with it before moving on to the next sentence. Don't forget to close the book when you're done!
line1 = file.readline()  # Reads the first line
line2 = file.readline()  # Reads the second line

# You can do things with each line you read. For example, you can print it, check if it contains specific words, or save it somewhere else.
print(line1)  # Print the first line
if 'important' in line2:
    print('This line is important!')

# Loop through lines
while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)

# When you're done reading, it's essential to close the file using file.close() to make sure you're not wasting resources.
file.close()

#If you only want to read specific characters: open file, navigate to desired position, read characters
file = open('file.txt', 'r')
# If you want to read characters from a specific position in the file, you can use the seek() method. This method moves the file pointer (like a cursor) to a particular position. 
# The position is specified in bytes, so you'll need to know the byte offset of the characters you want to read.
file.seek(10)  # Move to the 11th byte (0-based index)
# To read specific characters, you can use the read() method with an argument that specifies the number of characters to read. 
# It reads characters starting from the current position of the file pointer.
characters = file.read(5)  # Read the next 5 characters
#In this example, it reads the next 5 characters from the current position of the file pointer.
print(characters)
file.close()

# Pandas ===============================================================================

# Series in Pandas (a one dimensional labled array in Pandas, like a single column with indexes or labels)
import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

print(s)

print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label


# DataFrames (two-dimensional data structure with columns of different data types)
# DataFrames can be created from dictionaries, with keys as column labels and values as lists representing rows.
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)


# DataFrames =====================================================================

# Make a df from a dictionary
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)


print(df['Name'])  # Access the 'Name' column

# Access row with index
print(df.iloc[2])   # Access the third row by position

# Access second row by label
print(df.loc[1])    # Access the second row by label

# Slice df to select specific rows and columns
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# Find unique values in a column
unique_dates = df['Age'].unique()

# Filter with inequality operator
high_above_102 = df[df['Age'] > 25]

# Save df to csv file
df.to_csv('trading_data.csv', index=False)

# Numpy +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Installing Numpy
pip install numpy

# Import library
import numpy as np

# Create a 1D array
# Creating a 1D array ( a single line of elements)
# np.array() function to convert a Python list [1, 2, 3, 4, 5] into a NumPy array
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Array attributes
print(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# output : 2
print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# Output : (3, 3)
print(arr_2d.size) # size: Provides the total number of elements in the array.
# Output : 9

# Indexing and slicing
print(arr_1d[2])          # Accessing an element (3rd element)

print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)

print(arr_2d[1])          # Accessing a row (2nd row)

print(arr_2d[1])          # Accessing a row (2nd row)

print(arr_2d[:, 1])       # Accessing a column (2nd column)

# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9]

# Scalar multiplication
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]

# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]

# Square root each function
result = np.sqrt(arr)

# Calculating the sum and mean of an array.
total = np.sum(arr)<br>average = np.mean(arr)

# Finding the maximum and minimum values.
max_val = np.max(arr)<br>min_val = np.min(arr)

# Changing the shape of an array.
reshaped_arr = arr.reshape(2, 3)

# Transposing a multi-dimensional array.
transposed_arr = arr.T

# Performing matrix multiplication.
result = np.dot(matrix1, matrix2)

# *** Opening files with Python ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Different modes to open files for specific operations.
Examples: with open("data.txt", "r") as file: content = file.read() print(content) with open("output.txt", "w") as file: file.write("Hello, world!") with open("log.txt", "a") as file: file.write("Log entry: Something happened.") with open("data.txt", "r+") as file: content = file.read() file.write("Updated content: " + content)</td>

# Different methods to read file content in various ways.
file.readlines() # reads all lines as a list
readline() # reads the next line as a string
file.read() # reads the entire file content as a string

with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()

# Different write methods to write content to a file.
# Syntax
file.write(content) # writes a string to the file
file.writelines(lines) # writes a list of strings to the file
# Example
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Iterates through each line in the file using a `loop`.
# Syntax
for line in file: # Code to process each line
#Example
with open("data.txt", "r") as file:
for line in file: print(line)

# Opens a file, performs operations, and explicitly closes the file using the close() method.
# Syntax: 
file = open(filename, mode) # Code that uses the file
file.close()
# Example
file = open("data.txt", "r")
content = file.read()
file.close()

# Opens a file using a with block, ensuring automatic file closure after usage.
# Syntax
with open(filename, mode) as file: # Code that uses the file


# +++ Web Scraping Software ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Beautiful Soup ( python library to scrape HTML and XML pages)

Beautiful Soup ( python library for web scraping HTML and XML files)
from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Scrapy: Scrapy is an open-source and collaborative web crawling framework for Python. It is used to extract the data from the website.
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

# Selenium: Selenium is a tool used for controlling web browsers through programs and automating browser tasks.
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.example.com")

# Python has built in method to extract tables from web pages (.read_html)
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)

