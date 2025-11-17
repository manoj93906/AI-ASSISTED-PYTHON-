def assign_grade(score):
    """
    Returns a letter grade for the given score.
    90-100: A
    80-89:  B
    70-79:  C
    60-69:  D
    <60:    F
    Raises ValueError for invalid input.
    """
    if not isinstance(score, int):
        raise ValueError("Score must be an integer.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def generate_assign_grade_test_cases():
    """
    Generate test cases for assign_grade(score), including boundaries and invalid inputs.
    Returns a tuple: (valid_cases, invalid_cases)
    """
    # (input_score, expected_grade)
    valid_cases = [
        (100, "A"),
        (90, "A"),
        (99, "A"),
        (95, "A"),
        (89, "B"),
        (80, "B"),
        (85, "B"),
        (79, "C"),
        (70, "C"),
        (75, "C"),
        (69, "D"),
        (60, "D"),
        (65, "D"),
        (59, "F"),
        (0, "F"),
        (30, "F"),
    ]
    # Invalid scores: negative, over 100, wrong type
    invalid_cases = [-5, -1, 101, 150, "eighty", None, 90.1, [], {}]
    return valid_cases, invalid_cases

def test_assign_grade():
    valid_cases, invalid_cases = generate_assign_grade_test_cases()
    print("---- VALID INPUTS ----")
    for score, expected in valid_cases:
        try:
            result = assign_grade(score)
            print(f"assign_grade({score}) -> '{result}'  "
                  f"{'PASS' if result == expected else f'FAIL: expected {expected}'}")
        except Exception as e:
            print(f"assign_grade({score}) -> Exception: {e}")

    print("\n---- INVALID INPUTS ----")
    for score in invalid_cases:
        try:
            result = assign_grade(score)
            print(f"assign_grade({repr(score)}) -> '{result}'  FAIL (expected exception)")
        except Exception as e:
            print(f"assign_grade({repr(score)}) -> Exception: {e}  PASS")

def user_input_assign_grade():
    print("Enter a score to get letter grade, or 'quit' to exit.")
    while True:
        user_input = input("Score: ")
        if user_input.lower() == 'quit':
            break
        try:
            score = int(user_input)
            grade = assign_grade(score)
            print(f"Grade: {grade}")
        except Exception as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    print("=== Automated assign_grade Test Cases ===")
    test_assign_grade()
    print("\n=== Interactive assign_grade Demo ===")
    
