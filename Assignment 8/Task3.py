def generate_is_sentence_palindrome_test_cases():
    """
    AI-generated diverse test cases for is_sentence_palindrome(sentence).
    Ignores case, spaces, and punctuation in palindrome detection.
    Returns a list of tuples: (sentence, expected_result)
    """
    test_cases = [
        # Classic palindromic sentences
        ("A man a plan a canal Panama", True),
        ("Madam In Eden Im Adam", True),
        ("Was it a car or a cat I saw", True),
        ("No lemon, no melon", True),
        ("Eva, can I see bees in a cave?", True),
        ("Able was I ere I saw Elba", True),
        ("Never odd or even", True),
        ("Step on no pets!", True),
        ("Mr. Owl ate my metal worm", True),
        ("Do geese see God?", True),
        # Clearly not palindromes
        ("This is not a palindrome", False),
        ("OpenAI creates AI tools.", False),
        ("Hello world!", False),
        ("Palindrome", False),
        # Edge cases
        ("", True),  # Empty string is a palindrome by definition
        ("!", True), # Single punctuation
        ("   ", True), # Spaces only
        ("a", True), # Single character
        ("Madam, I'm Adam.", True),
        ("1234321", True), # Numeric palindrome
        ("12345", False),  # Numeric non-palindrome
        ("No 'x' in Nixon", True),
        ("Was it a bar or a bat I saw?", False), # Similar, but not a palindrome
        ("Go hang a salami! I'm a lasagna hog.", True),
    ]
    return test_cases

def test_is_sentence_palindrome(is_sentence_palindrome_func):
    """
    Runs test cases using the provided is_sentence_palindrome(sentence) function.
    """
    test_cases = generate_is_sentence_palindrome_test_cases()
    print("=== Testing is_sentence_palindrome(sentence) ===")
    for sentence, expected in test_cases:
        try:
            result = is_sentence_palindrome_func(sentence)
            outcome = "PASS" if result == expected else f"FAIL (expected {expected})"
        except Exception as e:
            result = f"Exception: {e}"
            outcome = "FAIL (unexpected exception)"
        print(f"Input: {repr(sentence):35}  --> {result}    {outcome}")

def user_input_is_sentence_palindrome(is_sentence_palindrome_func):
    print("\nEnter a sentence to test for palindrome (ignoring case, space, punctuation). Type 'quit' to exit.")
    while True:
        user_input = input("Sentence: ")
        if user_input.strip().lower() == "quit":
            break
        try:
            result = is_sentence_palindrome_func(user_input)
            print(f"Palindrome? {result}")
        except Exception as e:
            print(f"Error: {e}")

# Example minimal is_sentence_palindrome implementation for demonstration:
def is_sentence_palindrome(sentence):
    import string
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Automated tests
    test_is_sentence_palindrome(is_sentence_palindrome)
    # Interactive user input
   
