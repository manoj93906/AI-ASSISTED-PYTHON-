def grade(score):
    """
    Assign a letter grade based on score.
    
    Args:
        score (int/float): Numeric score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    # Dictionary mapping: minimum threshold -> grade
    grade_map = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        0: "F"  # Default case
    }
    
    # Find the appropriate grade by checking thresholds in descending order
    for threshold in sorted(grade_map.keys(), reverse=True):
        if score >= threshold:
            return grade_map[threshold]
    
    # Fallback (should not reach here if grade_map includes 0)
    return "F"


# Test the function
if __name__ == "__main__":
    test_scores = [95, 85, 75, 65, 55, 100, 90, 80, 70, 60, 0]
    
    for score in test_scores:
        result = grade(score)
        print(f"Score: {score:3d} -> Grade: {result}")
