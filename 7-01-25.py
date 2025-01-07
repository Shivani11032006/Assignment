n = int(input("Enter a positive integer: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    print("Sum of even numbers:", sum(num for num in range(2, n + 1, 2)))