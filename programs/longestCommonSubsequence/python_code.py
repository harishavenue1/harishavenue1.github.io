class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Python: Get string lengths
        len1 = len(text1)
        len2 = len(text2)
        
        # Python: List comprehension to create 2D DP table
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        
        # Python: Nested loops to fill DP table
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                
                # Python: Direct character comparison using indexing
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]  # Characters match
                else:
                    
                    # Python: Built-in max() function
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[len1][len2]
        