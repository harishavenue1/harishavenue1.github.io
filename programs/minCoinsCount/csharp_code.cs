public class Solution
{
    public int CoinChange(int[] coins, int amount)
    {
        
        // C#: Array initialization for DP
        int[] dp = new int[amount + 1];
        
        // C#: Array.Fill() initializes with impossible value
        Array.Fill(dp, amount + 1);
        
        // Base case: 0 coins needed for amount 0
        dp[0] = 0;
        
        
        // C#: foreach loop for each coin
        foreach (int coin in coins)
        {
            
            // C#: Standard for-loop from coin to amount
            for (int i = coin; i <= amount; i++)
            {
                
                // C#: Math.Min() to find minimum coins needed
                dp[i] = Math.Min(dp[i], dp[i - coin] + 1);
            }
        }
        
        
        // C#: Ternary operator for return value
        return (dp[amount] != amount + 1 ? dp[amount] : -1);
    }
}