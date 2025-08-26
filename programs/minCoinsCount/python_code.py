class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Python: List comprehension to create DP array with impossible values
        dp = [amount + 1] * (amount+1)
        
        # Base case: 0 coins needed for amount 0
        dp[0] = 0
        
        
        # Python: Direct iteration over coins list
        for coin in coins:
            
            # Python: range() for iteration from coin to amount+1
            for i in range(coin, amount+1):
                
                # Python: Built-in min() to find minimum coins needed
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        
        # Python: Conditional expression for return value
        return dp[amount] if dp[amount] != amount+1 else -1