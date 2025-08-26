package programs.climbStairDistinctWays;

class Solution {
    public int climbStairs(int n) {
        
        // Java: Dynamic programming - Fibonacci-like pattern
        // Base case: 1 way to climb 0 or 1 steps
        if (n <= 1)
            return 1;
            
        // Java: Space-optimized DP using variables instead of array
        int prev = 1, cur = 1, temp = 0;
        
        // Java: Build solution bottom-up from step 2 to n
        for (int i = 2; i <= n; i++) {
            
            // Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
            temp = prev + cur;
            prev = cur;         // Shift values for next iteration
            cur = temp;
        }
        
        return cur;
    }
}