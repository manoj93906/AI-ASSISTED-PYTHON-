def format_name(first, last):
    return f"{last}, {first}"

# Taking input from the user
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

# Formatting and printing the full name
formatted_name = format_name(first_name, last_name)
print("Formatted name:", formatted_name)
