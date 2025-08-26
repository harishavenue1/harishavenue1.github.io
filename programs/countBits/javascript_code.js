countBits = function (n) {
    
    // JavaScript: new Array() with .fill() to create array of zeros
    let arr = new Array(n + 1).fill(0)
    
    // JavaScript: Standard for-loop
    for (let i = 0; i < n + 1; i++) {
        
        // JavaScript: Bit manipulation - count bits using DP
        // arr[i >> 1] gets count for i/2, (i & 1) adds 1 if i is odd
        arr[i] = arr[i >> 1] + (i & 1)
    }
    
    return arr
};

let num = 2
console.log('For Num:', num, 'No of Bits are', countBits(num))
num = 5
console.log('For Num:', num, 'No of Bits are', countBits(num))