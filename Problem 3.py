"""
Project Euler #3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(number: int):
    """
    Give the largest prime factor of a number

    Args:
        number (int): Number to give factor

    Returns:
        int: Return a factor
    """

    if isinstance(number, int):
        for i in range(2, number // 4):
            if number % i == 0:
                if is_prime_number(number // i):
                    return number // i

    return 1

def is_prime_number(number: int):
    """
    Check if a number is prime or not

    Args:
        number (int): Number to check

    Returns:
        bool: Return whether the number is prime or not
    """

    if isinstance(number, int):
        if number == 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
            if i > number / 2:
                break

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
    print("*" * 7 + "Welcome to Euler Project #3" + "*" * 7)

    number_input = get_int_value_from_prompt("Enter the number: ")
    largest_prime_factor_output = largest_prime_factor(number_input)

    print(f"The largest prime factor of {number_input} is {largest_prime_factor_output}.")
