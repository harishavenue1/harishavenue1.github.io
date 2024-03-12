using System;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            int profit = MaxProfit(new int[] { 7, 1, 5, 3, 6, 4 });
            Console.WriteLine(profit);
        }

        public static int MaxProfit(int[] prices)
        {
            int maxProfit = 0;
            int leftIndex = 0, rightIndex = 0;
            int currentProfit = 0;

            while (rightIndex < prices.Length)
            {
                if (prices[rightIndex] > prices[leftIndex])
                {
                    currentProfit = prices[rightIndex] - prices[leftIndex];
                    maxProfit = Math.Max(maxProfit, currentProfit);
                }
                else
                {
                    leftIndex = rightIndex;
                }
                rightIndex++;
            }
            return maxProfit;
        }
    }
}
