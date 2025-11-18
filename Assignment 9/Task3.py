"""
AI-generated module-level docstring:

This module provides basic calculator functions: add, subtract, multiply, and divide. Each function takes two numerical arguments and returns the corresponding arithmetic operation result. The module also includes docstrings for each function that follow the NumPy documentation style.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float or int
        The first number to add.
    b : float or int
        The second number to add.

    Returns
    -------
    float or int
        The sum of the two numbers.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(-1, 5)
    4
    """
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float or int
        The number from which to subtract.
    b : float or int
        The number to subtract.

    Returns
    -------
    float or int
        The result after subtracting b from a.

    Examples
    --------
    >>> subtract(5, 2)
    3
    >>> subtract(0, 1)
    -1
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    float or int
        The product of the two numbers.

    Examples
    --------
    >>> multiply(3, 4)
    12
    >>> multiply(-2, 5)
    -10
    """
    return a * b

def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float or int
        The numerator.
    b : float or int
        The denominator.

    Returns
    -------
    float
        The result of dividing a by b.

    Raises
    ------
    ZeroDivisionError
        If b is zero.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    >>> divide(7, 3)
    2.3333333333333335
    """
    return a / b


# AI-GENERATED DOCSTRINGS FOR EACH FUNCTION (e.g. ChatGPT/Copilot)

def add_ai(a, b):
    """
    Adds two numbers and returns the result.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The sum of a and b.
    """
    return a + b

def subtract_ai(a, b):
    """
    Subtracts the second number from the first and returns the result.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The result of a minus b.
    """
    return a - b

def multiply_ai(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The product of a and b.
    """
    return a * b

def divide_ai(a, b):
    """
    Divides the first number by the second and returns the result.

    Parameters
    ----------
    a : int or float
        The dividend.
    b : int or float
        The divisor.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    return a / b

# -- Comparison of Docstrings: Manual vs. AI-generated (NumPy-style) --

# 1. **Clarity**:  
#    Manual docstrings tend to offer more context in the "Returns" section and provide practical usage examples. For example, they show concrete function calls and results, which greatly aid user understanding.  
#    AI-generated docstrings are clear but more generic, usually lacking usage examples.

# 2. **Formatting**:  
#    Both styles use NumPy formatting, but manual docstrings are sometimes more explicit about parameter order (e.g., clarifying which number is subtracted from which) and specify more detail ("the number from which to subtract" vs. "first operand").

# 3. **Detail**:  
#    Manual docstrings usually include examples, clarify edge cases, and detail exceptions (e.g., `ZeroDivisionError` in divide). AI-generated ones do mention exceptions, but are less comprehensive and sometimes too terse.

# 4. **Accuracy**:  
#    Both are accurate in describing the functions, but the manual ones are slightly superior due to more thorough examples and scenario coverage.

# -- Conclusion: --
#  
# Manual NumPy-style docstrings are more effective because they provide additional context, detailed examples, and clarify common use cases. Examples in particular make it easier for users to understand correct inputs and outputs. This improved communication outweighs the brevity and slight vagueness sometimes present in AI-generated docstrings.

if __name__ == "__main__":
    print("Simple Calculator Demo")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("add(a, b) =", add(a, b))
    print("subtract(a, b) =", subtract(a, b))
    print("multiply(a, b) =", multiply(a, b))
    try:
        print("divide(a, b) =", divide(a, b))
    except ZeroDivisionError:
        print("Cannot divide by zero.")
