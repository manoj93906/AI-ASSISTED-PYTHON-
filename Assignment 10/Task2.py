def find_common(a, b):
    """
    Find common elements between two lists using set intersection.
    
    Args:
        a: First list
        b: Second list
    
    Returns:
        List of common elements
    """
    return list(set(a) & set(b))


# Test the function
if __name__ == "__main__":
    # Example 1
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result1 = find_common(list1, list2)
    print(f"Common elements between {list1} and {list2}: {result1}")
