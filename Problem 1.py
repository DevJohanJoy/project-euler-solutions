"""
Project Euler #1
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples_of_two_factors_under_limit(
    first_factor: int, second_factor: int, limit: int):
    """
    Give the sum of all mutiples of the first or second factor inferior to the the limit

    Args:
        first_factor (int): First factor to check for multiples
        second_factor (int): Second factor to check for multiples
        limit (int): Limit of the multiples

    Returns:
        int: Return a sum
    """

    numbers_sum: int = 0
    
    if isinstance(first_factor, int) and isinstance(second_factor, int) and isinstance(limit, int):
        if first_factor > second_factor:
            max_factor = first_factor
            min_factor = second_factor
        else:
            max_factor = second_factor
            min_factor = first_factor

        print(min_factor)
        print(max_factor)

        i = 1
        while True:
            if min_factor * i >= limit:
                break

            if (min_factor * i) % max_factor != 0:
                numbers_sum += min_factor * i

            if max_factor * i < limit:
                numbers_sum += max_factor * i

            i += 1

    return numbers_sum

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
    print("*" * 7 + "Welcome to Euler Project #1" + "*" * 7)

    first_factor_input = get_int_value_from_prompt("Enter the first factor: ")
    second_factor_input = get_int_value_from_prompt("Enter the second factor: ")
    limit_input = get_int_value_from_prompt("Enter the limit: ")

    numbers_sum_output = sum_of_multiples_of_two_factors_under_limit(
        first_factor_input, second_factor_input, limit_input)

    print(f"The sum of all multiples of {first_factor_input} or {second_factor_input} " +
        f"under {limit_input} is {numbers_sum_output}")
