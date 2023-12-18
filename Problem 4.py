"""
Project Euler #4
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome_product_of_numders(number_of_digits: int):
    """
    Give the largest palindrome number product of a multiplication of two number

    Args:
        number_of_digits (int): Number of digits of the factors

    Returns:
        int: Return a palindrome
        None: Didn't find a palindrome
    """

    palindrome = 0

    if isinstance(number_of_digits, int):
        for i in range(10 ** number_of_digits - 1, 10 ** (number_of_digits - 1) - 1, -1):
            for j in range(10 ** number_of_digits - 1, 10 ** (number_of_digits - 1) - 1, -1):
                if is_palindrome(i * j) and i * j > palindrome:
                    palindrome = i * j

    if palindrome == 0:
        return None
    return palindrome

def is_palindrome(number: int):
    """
    Check if a number is palindrome or not

    Args:
        number (int): Number to check

    Returns:
        bool: Return whether the number is palindrome or not
    """

    if isinstance(number, int):
        return list(str(number)) == list(reversed(str(number)))

    return True

def get_int_value_from_prompt(msg: str):
    """
    Get an integer value from user input

    Args:
        msg (str): The prompt message to display

    Returns:
        int: The user input
    """

    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Please enter an integer!")


if __name__ == '__main__':
    print("*" * 7 + "Welcome to Euler Project #4" + "*" * 7)

    number_of_digits_input = get_int_value_from_prompt("Enter the number of digits for factors: ")
    largest_palindrome_output = largest_palindrome_product_of_numders(number_of_digits_input)

    if largest_palindrome_output is None:
        print("There are no palindrome numbers product from a multiplaction " +
              f"of two {number_of_digits_input}-digit numbers.")
    else:
        print("The largest palindrome product of a multiplication of two " +
          f"{number_of_digits_input}-digit numbers is {largest_palindrome_output}.")
