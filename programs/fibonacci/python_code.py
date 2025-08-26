def fibonacci(n):
    
    # Python: Tuple unpacking for multiple assignment
    a, b = 0, 1
    
    # Python: List to store Fibonacci sequence
    fib_sequence = []
    
    # Python: range() with underscore for unused variable
    for _ in range(n):
        
        # Python: .append() adds element to list
        fib_sequence.append(a)
        
        # Python: Elegant tuple unpacking for simultaneous assignment
        a, b = b, a + b
    return fib_sequence

print(fibonacci(10))
