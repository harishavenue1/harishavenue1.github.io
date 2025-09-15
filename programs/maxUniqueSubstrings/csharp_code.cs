using System;
using System.Collections.Generic;

public class Solution {
    /**
     * Find maximum number of unique substrings using backtracking
     */
    public int MaxUniqueSplit(string s) {
        return Backtrack(s, 0, new HashSet<string>());
    }
    
    private int Backtrack(string s, int start, HashSet<string> used) {
        if (start == s.Length) {
            return 0;
        }
        
        int maxCount = 0;
        for (int end = start + 1; end <= s.Length; end++) {
            string substring = s.Substring(start, end - start);
            if (!used.Contains(substring)) {
                used.Add(substring);
                int count = 1 + Backtrack(s, end, used);
                maxCount = Math.Max(maxCount, count);
                used.Remove(substring);
            }
        }
        
        return maxCount;
    }
}