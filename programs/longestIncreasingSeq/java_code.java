import java.util.Arrays;

public class java_code {

    public static void main(String[] args) {
        int[] arr = { 10, 9, 2, 5, 3, 7, 101, 18 };
        System.out.println("max seq length " + longestSeq(arr));

        arr = new int[] { 0, 1, 0, 3, 2, 3 };
        System.out.println("max seq length " + longestSeq(arr));

        arr = new int[] { 7, 7, 7, 7, 7, 7, 7 };
        System.out.println("max seq length " + longestSeq(arr));
    }

    public static int longestSeq(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxLength = Arrays.stream(dp).max().orElse(0);
        return maxLength;
        // return map.values().stream().max(Integer::compareTo).get();
    }
}
