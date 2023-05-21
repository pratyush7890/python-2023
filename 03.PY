def findNthMultipleInFibonacciSeries(n, num):
    # Returns the n-th multiple of num in the Fibonacci series.
    # If no such multiple exists, returns -1.
    a = 0
    b = 1
    for i in range(n):
        if a % num == 0:
            return a
        a, b = b, a + b
    return -1

# Example usage:
result = findNthMultipleInFibonacciSeries(5, 3)
if result == -1:
    print("No multiple of 3 found in the first 5 numbers of the Fibonacci series")
else:
    print(f"The 5th multiple of 3 in the Fibonacci series is {result}")
