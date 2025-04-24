def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


try:
    num = int(input("Enter the number of terms for the Fibonacci series: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series:", fibonacci_series(num))
except ValueError:
    print("Invalid input! Please enter an integer.")
