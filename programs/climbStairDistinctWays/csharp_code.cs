public class Solution {
    public int ClimbStairs(int n) {
        
        // C#: Dynamic programming - Fibonacci-like pattern
        // Base case: 1 way to climb 0 or 1 steps
        if (n <= 1)
            return 1;
        
        // C#: Explicit variable declarations
        int prev = 1;
        int cur = 1;
        int temp = 0;

        // C#: Standard for-loop with <= for inclusive range
        for (int i=2; i<=n; i++) {
            
            // Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
            temp = prev + cur;
            prev = cur;  // Shift values for next iteration
            cur = temp;
        }
        
        return cur;
    }
}