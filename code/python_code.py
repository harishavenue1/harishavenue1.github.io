def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
    a, b = b, a + b
    return fib_sequence

print(fibonacci(10))  # Change the value inside fibonacci() for different number of Fibonacci numbers
