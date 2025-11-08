def greet_user(name, gender):
    """
    Greets the user with an appropriate title based on gender.
    
    Supports 'male', 'female', and any other value defaults to gender-neutral 'Mx.'.
    """
    gender_lower = gender.lower()
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower == "female":
        title = "Mrs."
    else:
        title = "Mx."  # Gender-neutral title
    
    return f"Hello, {title} {name}! Welcome."


# Input prompts
name = input("Enter your name: ")
gender = input("Enter your gender (male/female/other): ")

# Greeting output
greeting = greet_user(name, gender)
print(greeting)
