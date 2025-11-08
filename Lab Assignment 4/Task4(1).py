def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Examples from prompt
print(count_vowels("hello"))        # Output: 2
print(count_vowels("world"))        # Output: 1
print(count_vowels("AI assistant")) # Output: 5
