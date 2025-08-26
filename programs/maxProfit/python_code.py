def maxProfit(prices):

    # Python: Two-pointer approach for buy/sell stock problem
    maxProfit = 0
    leftIndex = 0   # buy pointer
    rightIndex = 0  # sell pointer
    currentProfit = 0
    
    # Python: while loop with len() function
    while rightIndex < len(prices):

        # Check if we can make profit (sell > buy)
        if prices[rightIndex] > prices[leftIndex]:
            currentProfit = prices[rightIndex] - prices[leftIndex]
            
            # Python: Built-in max() function
            maxProfit = max(currentProfit, maxProfit)
        else:
            leftIndex = rightIndex  # Move buy pointer to lower price
            
        rightIndex += 1  # Always move sell pointer forward
        
    return maxProfit

mProfit = maxProfit([7,1,5,3,6,4])
print(mProfit)
