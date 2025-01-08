def calculate_square(n):
    return n * n  
def main():
    n = int(input("Enter a positive integer: "))
    result = calculate_square(n)
    print(f"The square of {n} is {result}")
if __name__ == "__main__":
    main()