package programs.longestIncreasingSequence;

import java.util.Arrays;

public class java_code {

    public static void main(String[] args) {
        System.out.println("=== LONGEST INCREASING SUBSEQUENCE ALGORITHM ===");
        
        int[] arr = { 10, 9, 2, 5, 3, 7, 101, 18 };
        System.out.println("\nTest 1: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));

        arr = new int[] { 0, 1, 0, 3, 2, 3 };
        System.out.println("\nTest 2: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));

        arr = new int[] { 7, 7, 7, 7, 7, 7, 7 };
        System.out.println("\nTest 3: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));
    }

    public static int longestSeq(int[] nums) {
        System.out.println("\nProcessing array: " + Arrays.toString(nums));
        
        if (nums == null || nums.length == 0) {
            System.out.println("Empty array, returning 0");
            return 0;
        }

        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        System.out.println("Initial DP array: " + Arrays.toString(dp));

        for (int i = 1; i < n; i++) {
            System.out.println("\nProcessing index " + i + ": nums[" + i + "] = " + nums[i]);
            for (int j = 0; j < i; j++) {
                System.out.print("  Comparing with nums[" + j + "] = " + nums[j]);
                if (nums[i] > nums[j]) {
                    int oldDp = dp[i];
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    System.out.println(" → " + nums[i] + " > " + nums[j] + ", dp[" + i + "] = max(" + oldDp + ", " + (dp[j] + 1) + ") = " + dp[i]);
                } else {
                    System.out.println(" → " + nums[i] + " ≤ " + nums[j] + ", no update");
                }
            }
            System.out.println("  Current DP: " + Arrays.toString(dp));
        }

        int maxLength = Arrays.stream(dp).max().orElse(0);
        System.out.println("Final DP array: " + Arrays.toString(dp));
        System.out.println("Maximum length: " + maxLength);
        return maxLength;

        // return map.values().stream().max(Integer::compareTo).get();
    }
}
