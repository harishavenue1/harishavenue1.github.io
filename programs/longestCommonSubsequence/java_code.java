public class java_code {
    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "ace";

        System.out.println("String 1: \"" + s1 + "\"");
        System.out.println("String 2: \"" + s2 + "\"");

        int result = longestCommonSubsequence(s1, s2);
        System.out.println("\nLongest Common Subsequence Length: " + result);
    }

    // Space-optimized iterative approach using only two arrays
    public static int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        // Use only two arrays instead of full 2D table
        int[] prev = new int[n + 1];
        int[] curr = new int[n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    curr[j] = prev[j - 1] + 1;
                } else {
                    curr[j] = Math.max(prev[j], curr[j - 1]);
                }
            }
            // Swap arrays for next iteration
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }

        return prev[n];
    }
}
