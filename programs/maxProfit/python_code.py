def maxProfit(prices):
    maxProfit = 0
    leftIndex = 0
    rightIndex = 0
    currentProfit = 0
    while rightIndex < len(prices):
        if prices[rightIndex] > prices[leftIndex]:
            currentProfit = prices[rightIndex] - prices[leftIndex]
            maxProfit = max(currentProfit, maxProfit)
        else:
            leftIndex = rightIndex
        rightIndex+=1
    return maxProfit

mProfit = maxProfit([7,1,5,3,6,4])
print(mProfit)
