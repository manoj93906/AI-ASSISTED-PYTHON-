def linear_search(values, target):
    """Return the index of target in values using linear search."""
    for idx, value in enumerate(values):
        if value == target:
            return idx
    return -1


if __name__ == "__main__":
    data = [5, 3, 8, 6, 7, 2]
    key = 6
    result = linear_search(data, key)

    if result != -1:
        print(f"Value {key} found at index {result}")
    else:
        print(f"Value {key} not found in the list")
