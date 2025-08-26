package programs.minCoinsCount;

import java.util.Arrays;

public class java_code {

    public static void main(String[] args) throws Exception {
        int[] coins = { 1, 2, 5 };
        int targetAmount = 11;
        int output = coinChange(coins, targetAmount);
        System.out.println("Least Coins Required are " + output);
    }

    public static int coinChange(int[] coins, int amount) {
        
        // Java: DP array to store minimum coins for each amount
        int[] dp = new int[amount + 1];
        
        // Java: Arrays.fill() initializes with impossible value
        Arrays.fill(dp, amount + 1);
        
        // Base case: 0 coins needed for amount 0
        dp[0] = 0;
        
        
        // Java: Enhanced for-loop for each coin
        for (int coin : coins) {
            
            // Java: Standard for-loop from coin value to target amount
            for (int i = coin; i <= amount; i++) {
                
                // Java: Math.min() to find minimum coins needed
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        
        
        // Java: Return result or -1 if impossible
        return (dp[amount] != amount + 1 ? dp[amount] : -1);
    }
}
