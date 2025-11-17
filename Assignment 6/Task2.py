def print_multiples(number):
    """
    Calculates and prints the first 10 multiples of a given number.

    Args:
        number (int or float): The number for which to print multiples.
    """
    if not isinstance(number, (int, float)):
        print("Error: Input must be a number.")
        return

    print(f"--- The first 10 multiples of {number} ---")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# --- Example Usage ---

# Example 1: Using an integer
print("Example with the number 8:")
print_multiples(8)

print("\n" + "="*30 + "\n")

# Example 2: Using a floating-point number
print("Example with the number 4.5:")
print_multiples(4.5)
