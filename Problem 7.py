"""
Project Euler #7
https://projecteuler.net/problem=7

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def prime_number_at_the_position(position: int):
    """
    Give the prime number at that position

    Args:
        psotion (int): Position of the prime number

    Returns:
        int: Return a prime number
    """

    i = 1
    prime_number = 2
    while i < position:
        prime_number += 1
        if is_prime_number(prime_number):
            i += 1

    return prime_number

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
    print("*" * 7 + "Welcome to Euler Project #7" + "*" * 7)

    position_input = get_int_value_from_prompt("Position: ")
    prime_number_output = prime_number_at_the_position(position_input)

    print(f"The {position_input}st prime number is {prime_number_output}.")
