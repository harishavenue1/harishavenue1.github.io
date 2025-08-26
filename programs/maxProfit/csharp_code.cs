using System;

class Program
{
    public static void Main(string[] args)
    {
        int profit = MaxProfit(new int[] { 7, 1, 5, 3, 6, 4 });
        Console.WriteLine(profit);
    }

    public static int MaxProfit(int[] prices)
    {

        // C#: Two-pointer approach for buy/sell stock problem
        int maxProfit = 0;
        int leftIndex = 0, rightIndex = 0;  // left = buy, right = sell
        int currentProfit = 0;

        // C#: while loop with .Length property (capital L)
        while (rightIndex < prices.Length)
        {

            // Check if we can make profit (sell > buy)
            if (prices[rightIndex] > prices[leftIndex])
            {
                currentProfit = prices[rightIndex] - prices[leftIndex];
                
                // C#: Math.Max() static method
                maxProfit = Math.Max(maxProfit, currentProfit);
            }
            else
            {
                leftIndex = rightIndex;  // Move buy pointer to lower price
            }
            
            rightIndex++;  // Always move sell pointer forward
        }
        
        return maxProfit;
    }
}
