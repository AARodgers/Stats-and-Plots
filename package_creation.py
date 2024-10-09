# Notes on how to create packages in python

# Objectives: 
# Create a module named basic
# Add two functions to the module basic
# Create a module named stats
# Add two functions to the module stats
# Create a python package named mymath
# Verify that the package is working

# Note: these are just notes on the lab, will be using mymath folder and files for exercises

1. Create a folder called mymath
2. In it, create two python files or modules called basic.py and stats.py and write your codes
3. In terminal, type: 'python3'  to invoke the python interpreter
4. In the python interpreter prompt type: 'import mymath'  or in otherwords import <foldername> ( if you get no errors, the package loaded successfully)
5. In python prompt type:  mymath.basic.add(3, 4), should get 7
6. Try doing: mymath.stats.mean([3, 4, 5]), should get 4
7. Type: 'exit()' to get out of python interpreter prompt or Ctrl + DeprecationWarning


More steps: 
Create a module name geometry
Add a function named area_of_rectangle that takes length and breadth as input and returns the area of a rectangle.
Add a function named area_of_circle that takes radius as input and returns the area of a circle.
Modify the __init__.py to include this module.
Import and test the function area_of_circle from python terminal.

1. After creating functions in geometry.py file ( make sure to import math)
2. open python prompt: in terminal: 'python3'
3. Type: 'import mymath'
4. Type: 'mymath.geometry.area_of_circle(2)' to find area of circel with radius 2
