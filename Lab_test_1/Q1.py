def fibonacci(n):

    """Generate Fibonacci sequence up to n terms."""

    sequence = [0, 1]

    for i in range(2, n):

        sequence.append(sequence[i-1] + sequence[i-2])

    return sequence[:n]



while True:

    try:

        n = int(input("Enter number of terms (positive integer): "))

        if n <= 0:

            print("Please enter a positive integer.")

            continue

        print("Fibonacci sequence:")

        print(fibonacci(n))

        break

    except ValueError:

        print("Invalid input. Please enter a positive integer.")

