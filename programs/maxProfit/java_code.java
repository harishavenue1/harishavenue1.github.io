package programs.maxProfit;

class java_code 
{
    public static int maxProfit(int[] prices) 
    {
        
        // Java: Two-pointer approach for buy/sell stock problem
        int maxProfit = 0;
        int leftIndex = 0, rightIndex = 1;  // left = buy, right = sell
        int currentProfit = 0;
        
        
        // Java: while loop with .length field
        while (rightIndex < prices.length) 
        {
            
            // Check if we can make profit (sell > buy)
            if (prices[rightIndex] > prices[leftIndex]) 
            {
                currentProfit = prices[rightIndex] - prices[leftIndex];
                
                
                // Java: Math.max() to track maximum profit
                maxProfit = Math.max(currentProfit, maxProfit);
            } 
            else
                leftIndex = rightIndex;  // Move buy pointer to lower price

            rightIndex++;  // Always move sell pointer forward
        }
        
        return maxProfit;
    }

    public static void main(String[] args) 
    {
        int profit = maxProfit(new int[] { 7, 6, 4, 3, 1 });
        System.out.println(profit);
    }
}
