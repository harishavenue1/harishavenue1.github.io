var reverseBits = function (n) {
    
    // JavaScript: Initialize result for reversed bits
    let result = 0
    
    // JavaScript: Process all 32 bits
    for (let i = 0; i < 32; i++) {
        
        // JavaScript: Shift result left and add current bit
        result *= 2
        result += n & 1
        
        // JavaScript: Right shift to process next bit
        n >>= 1
    }
    
    return result
};