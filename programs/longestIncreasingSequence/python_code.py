class Solution:
    def longestSeq(nums):
        
        # Python: Get array length
        arrLen = len(nums)
        
        # Python: DP array initialized with 1s (each element forms sequence of length 1)
        dp = [1] * arrLen

        
        # Python: Fill DP table using nested loops
        for i in range(arrLen):
            for j in range(0, i):
                
                # Python: Check if current element can extend previous sequence
                if nums[i] > nums[j]:
                    
                    # Python: Built-in max() to update longest sequence ending at i
                    dp[i] = max(dp[i], dp[j]+1)
        
        
        # Python: Built-in max() to find overall longest sequence
        return max(dp)