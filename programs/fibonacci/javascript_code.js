function fibonacci(n) {
    
    // JavaScript: let for block-scoped variables
    let a = 0, b = 1, sum = 0;
    
    // JavaScript: Standard for-loop
    for (let i = 0; i < n; i++) {
        
        // JavaScript: console.log() for output
        console.log(a);
        
        // Calculate next Fibonacci number: F(n) = F(n-1) + F(n-2)
        sum = a + b;
        a = b;
        b = sum;
    }
}

fibonacci(10)