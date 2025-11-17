def count_down(n):
    while n >= 0:
        print(n)
        n -= 1   # Correct decrement

# Taking input from user
num = int(input("Enter a number to countdown from: "))
count_down(num)
