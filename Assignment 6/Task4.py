def sum_to_n(n):
    """
    Calculates the sum of all integers from 1 to n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int or str: The sum of integers from 1 to n, or an error message string
                    if the input is invalid.
    """
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer."

    # Using the mathematical formula for the sum of the first n integers for efficiency.
    return n * (n + 1) // 2

# --- Example Usage ---
print("--- Calculating the Sum of the First N Numbers ---")

test_values = [10, 100, 0, -5, 9.5, "hello"]
for value in test_values:
    result = sum_to_n(value)
    print(f"Input: {value} -> Result: {result}")
