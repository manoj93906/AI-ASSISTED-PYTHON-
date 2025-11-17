numbers = [1, 2, 3]

# Corrected safe-access code with user input
index = int(input("Enter an index (0–2): "))

if 0 <= index < len(numbers):
    print("Value:", numbers[index])
else:
    print("Error: index out of range.")
