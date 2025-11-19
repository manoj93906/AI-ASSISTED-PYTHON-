def divide_numbers(a, b):
    """
    Divide two numbers with proper error handling.
    
    This function performs division of two numbers and handles common edge cases:
    - Division by zero (ZeroDivisionError): Returns a user-friendly error message
    - Invalid input types (TypeError): Handles cases where non-numeric values are passed
    - General exceptions: Catches any unexpected errors during division
    
    Args:
        a (float/int): The dividend (number to be divided)
        b (float/int): The divisor (number to divide by)
    
    Returns:
        float: The result of the division (a / b)
    
    Raises:
        ZeroDivisionError: When b is zero, prints an error message and returns None
        TypeError: When non-numeric values are provided, prints an error message and returns None
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(10, 0)
        Error: Division by zero is not allowed.
        None
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError as e:
        print(f"Error: Invalid input type. Both arguments must be numbers. {e}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred during division: {e}")
        return None

# Test the function
if __name__ == "__main__":
    # Test case 1: Normal division
    print("Test 1: Normal division")
    result1 = divide_numbers(10, 2)
    print(f"10 / 2 = {result1}")
    print()
    
    # Test case 2: Division by zero (original problematic case)
    print("Test 2: Division by zero")
    result2 = divide_numbers(10, 0)
    print(f"10 / 0 = {result2}")
    print()
    
    # Test case 3: Division with float result
    print("Test 3: Division with float result")
    result3 = divide_numbers(10, 3)
    print(f"10 / 3 = {result3}")
    print()
    
    # Test case 4: Invalid input type
    print("Test 4: Invalid input type")
    result4 = divide_numbers(10, "abc")
    print(f"10 / 'abc' = {result4}")
    print()
    
    # Test case 5: Negative numbers
    print("Test 5: Division with negative numbers")
    result5 = divide_numbers(-10, 5)
    print(f"-10 / 5 = {result5}")
