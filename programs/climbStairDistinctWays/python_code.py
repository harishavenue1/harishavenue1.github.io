class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Python: Dynamic programming - Fibonacci-like pattern
        # Base case: 1 way to climb 0 or 1 steps
        if n <= 1:
            return 1
        
        # Python: Tuple unpacking for multiple variable assignment
        prev, cur, temp = 1, 1, 0

        # Python: range(start, end+1) for inclusive iteration
        for i in range(2, n+1):
            
            # Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
            temp = prev + cur
            prev = cur  # Shift values for next iteration
            cur = temp
        
        return cur