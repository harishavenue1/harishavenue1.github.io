/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    
    // JavaScript: Dynamic programming - Fibonacci-like pattern
    // Base case: 1 way to climb 0 or 1 steps
    if (n <= 1)
        return 1

    
    // JavaScript: let for block-scoped variables
    let prev = 1
    let cur = 1
    let temp = 0

    
    // JavaScript: Standard for-loop with <= for inclusive range
    for (let i = 2; i <= n; i++) {
        
        // Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
        temp = prev + cur
        
        // Shift values for next iteration
        prev = cur
        cur = temp
    }

    return cur;
};