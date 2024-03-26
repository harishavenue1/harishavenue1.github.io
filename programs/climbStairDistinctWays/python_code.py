class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        prev, cur, temp = 1, 1, 0

        for i in range(2, n+1):
            temp = prev + cur
            prev = cur
            cur = temp
        
        return cur