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
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return (dp[amount] != amount + 1 ? dp[amount] : -1);
    }
}
