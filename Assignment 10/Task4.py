def calculate_average(scores):
    """
    Calculate the average of a list of scores.
    
    Args:
        scores (list): List of numeric scores
    
    Returns:
        float: Average of all scores
    """
    if not scores:
        raise ValueError("Cannot calculate average of empty list")
    return sum(scores) / len(scores)

def find_highest(scores):
    """
    Find the highest score in a list.
    
    Args:
        scores (list): List of numeric scores
    
    Returns:
        float/int: Highest score
    """
    if not scores:
        raise ValueError("Cannot find highest in empty list")
    
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def find_lowest(scores):
    """
    Find the lowest score in a list.
    Args:
        scores (list): List of numeric scores
    Returns:
        float/int: Lowest score
    """
    if not scores:
        raise ValueError("Cannot find lowest in empty list")
    lowest = scores[0]
    for score in scores:
        if score < lowest:
            lowest = score
    return lowest

def process_scores(scores):
    """
    Process a list of scores and display statistics.
    Args:
        scores (list): List of numeric scores
    """
    if not scores:
        print("No scores to process")
        return
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

# Test the functions
if __name__ == "__main__":
    # Example 1
    test_scores1 = [85, 92, 78, 96, 88, 90]
    print("Test Scores 1:", test_scores1)
    process_scores(test_scores1)
    print()
