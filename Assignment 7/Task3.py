def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero is not allowed."

# Example 1
print(divide(10, 0))   # division by zero case

# Example 2
print(divide(20, 5))   # valid division
