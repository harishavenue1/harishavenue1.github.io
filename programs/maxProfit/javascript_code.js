var maxProfit = function (prices) {
    let maxProfit = 0
    let currentProfit = 0
    let leftIndex = 0
    let rightIndex = 0

    while (rightIndex < prices.length) {
        if (prices[rightIndex] > prices[leftIndex]) {
            currentProfit = prices[rightIndex] - prices[leftIndex];
            maxProfit = Math.max(currentProfit, maxProfit);
        }
        else {
            leftIndex = rightIndex;
        }
        rightIndex += 1;
    }
    return maxProfit
};

let profit = maxProfit([7, 6, 4, 3, 1]);
console.log(profit);
