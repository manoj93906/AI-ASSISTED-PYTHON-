def convert_date_format(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY'.
    Example: '2023-10-15' -> '15-10-2023'
    """
    try:
        parts = date_str.split("-")
        if len(parts) != 3:
            raise ValueError("Input must be in 'YYYY-MM-DD' format")
        yyyy, mm, dd = parts
        if not (len(yyyy) == 4 and len(mm) == 2 and len(dd) == 2):
            raise ValueError("Elements must be of correct length")
        int(yyyy), int(mm), int(dd)  # Validate numeric
        return f"{dd}-{mm}-{yyyy}"
    except Exception:
        raise ValueError(f"Invalid date format: '{date_str}'")

def test_convert_date_format():
    """
    Run automated test cases for convert_date_format.
    """
    test_cases = [
        # (input, expected_output)
        ("2023-10-15", "15-10-2023"),
        ("2000-01-01", "01-01-2000"),
        ("1999-12-31", "31-12-1999"),
        ("2021-05-09", "09-05-2021"),
        ("2022-06-20", "20-06-2022"),
    ]
    print("Automated test cases:")
    for date_in, expected in test_cases:
        try:
            out = convert_date_format(date_in)
            result = "PASS" if out == expected else f"FAIL (got '{out}', expected '{expected}')"
        except Exception as e:
            result = f"FAIL (exception: {e})"
        print(f"Input: {date_in} -> Output: {convert_date_format(date_in)} [{result}]")

    # Test invalid cases
    invalids = [
        "20231015",     # No dashes
        "2023-15-10",   # Invalid month
        "23-10-15",     # Year has wrong length
        "2023-10",      # Incomplete
        "2023-10-015",  # Day extra digit
        "abcd-ef-gh",   # Not numbers
        "",             # Empty
        "2023-02-30",   # Valid format but invalid date (no validation here)
    ]
    print("\nInvalid input cases (should raise ValueError):")
    for bad in invalids:
        try:
            _ = convert_date_format(bad)
            print(f"Input: {bad} -> FAIL (should have raised error)")
        except ValueError:
            print(f"Input: {bad} -> PASS (raised ValueError)")
        except Exception as e:
            print(f"Input: {bad} -> FAIL (unexpected exception: {e})")

def user_input_convert_date_format():
    """
    Let users enter date strings to convert.
    """
    print("\nEnter date in 'YYYY-MM-DD' to convert to 'DD-MM-YYYY'. Type 'quit' to exit.")
    while True:
        user = input("Enter date: ")
        if user.strip().lower() == "quit":
            break
        try:
            converted = convert_date_format(user)
            print(f"Converted: {converted}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_convert_date_format()
    
