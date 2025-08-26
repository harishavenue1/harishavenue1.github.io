/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
    
    // JavaScript: new Array() with .fill() to create DP array
    let dp = new Array(amount + 1).fill(amount + 1)
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0
    
    
    // JavaScript: for-of loop for each coin
    for (let coin of coins) {
        
        // JavaScript: Standard for-loop from coin to amount
        for (let i = coin; i <= amount; i++) {
            
            // JavaScript: Math.min() to find minimum coins needed
            dp[i] = Math.min(dp[i], dp[i - coin] + 1)
        }
    }
    
    
    // JavaScript: Ternary operator for return value
    return (dp[amount] != amount + 1 ? dp[amount] : -1)
};