package programs.longestCommonSubsequence;

public class java_code {

    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "ace";
        System.out.println(longestCommonSubsequence(s1, s2));
    }

    public static int longestCommonSubsequence(String text1, String text2) {
        
        // Java: Get string lengths
        int length1 = text1.length();
        int length2 = text2.length();

        
        // Java: 2D DP array with extra row/column for base case
        int[][] dp = new int[length1 + 1][length2 + 1];

        
        // Java: Fill DP table using nested loops
        for (int i = 1; i <= length1; i++) {
            for (int j = 1; j <= length2; j++) {
                
                // Java: .charAt() to compare characters
                if (text1.charAt(i - 1) == text2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1] + 1;  // Characters match
                else
                    
                    // Java: Math.max() to take maximum of two options
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        
        return dp[length1][length2];
    }
}
