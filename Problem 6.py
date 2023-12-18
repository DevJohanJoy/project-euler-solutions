"""
Project Euler #6
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is, (1^2 + 2^2 + ... + 10^2) = 385.
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 3025,

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
"""

def difference_of_sum_of_squares_and_square_of_sum_under_limit(limit: int):
    """
    Give the difference of the sum of all squares numbers and the squares of
    the sum of all numbers inferior or equal to the limit

    Args:
        limit (int): Limit of the sums

    Returns:
        int: Return a difference
    """

    squares_of_sum = 0
    sum_of_squares = 0

    if isinstance(limit, int):
        for i in range(1, limit + 1):
            squares_of_sum += i
            sum_of_squares += i ** 2

        squares_of_sum **= 2

    return squares_of_sum - sum_of_squares

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
    print("*" * 7 + "Welcome to Euler Project #6" + "*" * 7)

    limit_input = get_int_value_from_prompt("Enter the limit: ")

    difference_output = difference_of_sum_of_squares_and_square_of_sum_under_limit(limit_input)

    print("The difference between the square of the sum and the sum of "
        + f"the squares of the firsts {limit_input} natural numbers is {difference_output}")
