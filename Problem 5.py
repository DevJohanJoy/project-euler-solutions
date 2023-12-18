"""
Project Euler #5
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def min_number_divided_by_all_numbers_under_limit(limit: int):
    """
    Give the min number which can be evenly divided by all integers under the limit

    Args:
        limit (int): Limit of the factors

    Returns:
        int: Return a the multiple
    """

    factors = list(range(1, limit + 1))
    factors_prime = [x for x in factors if is_prime_number(x)]
    remained_factors = [x for x in factors if x not in factors_prime]
    min_multiple = 1

    for i in factors_prime:
        min_multiple *= i

    while len(remained_factors) > 0:
        if min_multiple % remained_factors[0] != 0:
            for i in factors_prime:
                if (min_multiple * i) % remained_factors[0] == 0:
                    min_multiple *= i
                    break
                if i == factors_prime[-1]:
                    min_multiple *= remained_factors[0]

        remained_factors.remove(remained_factors[0])

    return min_multiple

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
    print("*" * 7 + "Welcome to Euler Project #5" + "*" * 7)

    max_factor_input = get_int_value_from_prompt("Max factor: ")
    min_multiple_output = min_number_divided_by_all_numbers_under_limit(max_factor_input)

    print("The min number who can evenly be divided by all integers from 1 to "
        + f"{max_factor_input} is {min_multiple_output}.")
