var maxProfit = function (prices) {
    
    // JavaScript: Two-pointer approach for buy/sell stock problem
    let maxProfit = 0
    let currentProfit = 0
    
    // buy pointer and sell pointer
    let leftIndex = 0
    let rightIndex = 0

    
    // JavaScript: while loop with .length property
    while (rightIndex < prices.length) {
        
        // Check if we can make profit (sell > buy)
        if (prices[rightIndex] > prices[leftIndex]) {
            currentProfit = prices[rightIndex] - prices[leftIndex];
            
            
            // JavaScript: Math.max() static method
            maxProfit = Math.max(currentProfit, maxProfit);
        }
        else {
            
            // Move buy pointer to lower price
            leftIndex = rightIndex;
        }
        
        
        // Always move sell pointer forward
        rightIndex += 1;
    }
    
    return maxProfit
};

let profit = maxProfit([7, 6, 4, 3, 1]);
console.log(profit);
