#positive integer
n = int(input("Enter a positive integer n: "))
print("Numbers from 1 to", n, "using for loop:")
for i in range(1, n + 1):
    print(i)

sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1

print("Sum of numbers from 1 to", n, "using while loop:", sum_numbers)
