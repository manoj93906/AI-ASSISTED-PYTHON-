def classify_age(age):
    """
    Classifies an individual into an age group using nested conditionals.

    Args:
        age (int): The age of the individual.

    Returns:
        str: The age group classification.
    """
    if not isinstance(age, int) or age < 0:
        return "Invalid age. Please provide a non-negative integer."

    if age < 1:
        return "Infant"
    elif age < 3:
        return "Toddler"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 40:
        return "Young Adult"
    elif age < 65:
        return "Middle-aged Adult"
    else:
        return "Senior"

# --- Example Usage ---
ages_to_test = [-1, 0, 2, 10, 16, 25, 45, 70]

print("--- Age Group Classification Examples ---")
for current_age in ages_to_test:
    classification = classify_age(current_age)
    print(f"Age: {current_age} -> Classification: {classification}")
