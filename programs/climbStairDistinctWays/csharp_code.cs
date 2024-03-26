public class Solution {
    public int ClimbStairs(int n) {
        if (n <= 1)
            return 1;
        
        int prev = 1;
        int cur = 1;
        int temp = 0;

        for (int i=2; i<=n; i++) {
            temp = prev + cur;
            prev = cur;
            cur = temp;
        }
        return cur;
    }
}