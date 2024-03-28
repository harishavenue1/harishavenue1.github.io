class Solution:
    def longestSeq(nums):
        arrLen = len(nums)
        dp = [1] * arrLen

        for i in range(arrLen):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)