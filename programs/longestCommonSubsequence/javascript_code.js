/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
    
    // JavaScript: Get string lengths using .length property
    len1 = text1.length
    len2 = text2.length
    
    // JavaScript: Create 2D array using .fill() and .map()
    dp = new Array(len1 + 1).fill(0).map(() => new Array(len2 + 1).fill(0))

    
    // JavaScript: Nested loops to fill DP table
    for (let i = 1; i <= len1; i++) {
        for (let j = 1; j <= len2; j++) {
            
            // JavaScript: Direct character comparison using indexing
            if (text1[i - 1] == text2[j - 1])
                dp[i][j] = 1 + dp[i - 1][j - 1]  // Characters match
            else
                
                // JavaScript: Math.max() for maximum value
                dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j])
        }
    }
    
    return dp[len1][len2]
};