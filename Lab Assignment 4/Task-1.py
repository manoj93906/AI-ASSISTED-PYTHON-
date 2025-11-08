def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    A year is a leap year if it is:
    - Divisible by 4 AND
    - Not divisible by 100 OR divisible by 400
    """
    # Check if year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, it must also be divisible by 400 to be a leap year
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Example usage:
if _name_ == "_main_":
    # Test cases
    test_years = [2000, 2020, 2024, 1900, 2100, 2023]
    
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year} is{' ' if result else ' not '}a leap year")
