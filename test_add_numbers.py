# Import the testing framework and the function to be tested
import pytest
from add_numbers import add_numbers

# Write the test function
def test_add_numbers():
    # Test case 1: Test addition of two positive numbers
    assert add_numbers(10, 20) == 30

    # Test case 2: Test addition of two negative numbers
    assert add_numbers(-10, -20) == -30

    # Test case 3: Test addition of a positive and a negative number
    assert add_numbers(10, -20) == -10

    # Test case 4: Test addition of zero and a number
    assert add_numbers(0, 10) == 10