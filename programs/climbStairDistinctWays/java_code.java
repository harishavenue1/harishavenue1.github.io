package programs.climbStairDistinctWays;

class Solution {
    public int climbStairs(int n) {
        if (n <= 1)
            return 1;
        int prev = 1, cur = 1, temp = 0;
        for (int i = 2; i <= n; i++) {
            temp = prev + cur;
            prev = cur;
            cur = temp;
        }
        return cur;
    }
}