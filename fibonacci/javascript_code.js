function fibonacci(n) {
    let a = 0, b = 1, sum = 0;
    for (let i = 0; i < n; i++) {
        console.log(a);
        sum = a + b;
        a = b;
        b = sum;
    }
}

fibonacci(10)