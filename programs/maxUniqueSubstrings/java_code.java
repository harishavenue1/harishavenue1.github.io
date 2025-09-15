import java.util.*;

public class Solution {
    /**
     * Find maximum number of unique substrings using backtracking
     */
    public int maxUniqueSplit(String s) {
        return backtrack(s, 0, new HashSet<>());
    }

    private int backtrack(String s, int start, Set<String> used) {
        if (start == s.length()) {
            return 0;
        }

        int maxCount = 0;

        for (int end = start + 1; end <= s.length(); end++) {
            String substring = s.substring(start, end);

            if (!used.contains(substring)) {
                used.add(substring);
                int count = 1 + backtrack(s, end, used);
                maxCount = Math.max(maxCount, count);
                used.remove(substring);
            }
        }

        return maxCount;
    }
}