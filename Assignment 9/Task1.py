def sum_even_odd(numbers):
    """
    Sums the even and odd numbers from a given list of integers.

    Args:
        numbers (list of int): A list of integer numbers.

    Returns:
        tuple: A tuple containing two elements:
            - int: The sum of all even numbers in the list.
            - int: The sum of all odd numbers in the list.

    Example:
        >>> sum_even_odd([1, 2, 3, 4])
        (6, 4)
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# AI-generated docstring:
"""
Calculates the sum of even and odd numbers in a list.

Parameters:
    numbers (list): A list of integers.

Returns:
    tuple: A tuple with the sum of even numbers as the first element and sum of odd numbers as the second element.
"""

# -- Comparison of Docstrings --
# The manually written docstring includes precise type hints, an example, and a structured Google style, making it clearer and more helpful for users and tools.
# The AI-generated docstring is shorter but less detailed; it lacks a usage example and does not specify the element type of the input as precisely.
# Overall, the manual docstring is more effective for both users and developers due to its clarity, completeness, and concrete example.

if __name__ == "__main__":
    user_input = input("Enter a list of integers separated by spaces: ")
    num_list = list(map(int, user_input.strip().split()))
    even, odd = sum_even_odd(num_list)
    print("Sum of even numbers:", even)
    print("Sum of odd numbers:", odd)
