function fibonacci(n) {
    let a = 0, b = 1;
    let fibArray = [];
    for (let i = 0; i < n; i++) {
        fibArray.push(a);
        let temp = a;
        a = b;
        b = temp + b;
    }
    return fibArray;
}

console.log(fibonacci(10)); // Change the value inside fibonacci() for different number of Fibonacci numbers