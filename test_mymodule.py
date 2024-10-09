# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
# unit_testing is the other file that has your code in it that you want to test and square and double are the functions that you are testing
from unit_testing import square, double

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.

        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'double(-3.1)' returns -6.2.
        # This tests if the function correctly computes double of -3.1, verifying that it handles negative float inputs.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.

        # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

# Define a test case class for testing the 'add' function.
class TestAdd(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'add(2, 4)' returns 6.
        # This tests if the function correctly computes the addition of two positive integers.
        self.assertEqual(add(2, 4), 6) # test when (2,4) is given as input the output is 6.

        # Check that calling 'addd(0,0)' returns 0.
        # This tests if the function correctly computes the addition of 0 and 0, verifying that it handles edge cases with 0.
        self.assertEqual(add(0,0), 0) # test when (0,0) is given as input the output is 0.

        # Check that calling 'add(2.3, 3.6)' returns 5.9.
        # This tests if the function correctly computes the addition of 2.3 and 3.6, verifying that the function works for floats.
        self.assertEqual(add(2.3, 3.6), 5.9) # test when 2.3, 3.6 is given as input the output is 5.9.

        # Check that calling 'add('hello', 'world')' returns helloworld.
        # This tests if the function correctly concanenates 'hello' and 'world', verifying that the function works for strings.
        self.assertEqual(add(2.3, 3.6), 5.9) # test when 'hello', 'world' is given as input the output is helloworld.

        # Check that calling 'add('2.3000', '4.300')' returns 6.6.
        # This tests if the function correctly adds '2.3000' and '4.300', verifying that the function works for 3 decimal points.
        self.assertEqual(add(2.3000, 4.300), 6.6) # test when '2.3000', '4.300' is given as input the output is 6.6.

        # Check that calling 'add('-2', '-2')' returns NOT 0.
        # This tests if the function correctly adds '-2' and '-2', verifying that the function does not return 0 for two negative numbers.
        self.assertNotEqual(add(-2, -2), 0) # test when '-2', '-2' is given as input the output is NOT 0.
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()



# In terminal, to run the test: 
# run file: python3 test_mymodule.py
