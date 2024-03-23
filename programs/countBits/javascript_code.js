countBits = function (n) {
    let arr = new Array(n + 1).fill(0)
    for (let i = 0; i < n + 1; i++) {
        arr[i] = arr[i >> 1] + (i & 1)
    }
    return arr
};

let num = 2
console.log('For Num:', num, 'No of Bits are', countBits(num))
num = 5
console.log('For Num:', num, 'No of Bits are', countBits(num))