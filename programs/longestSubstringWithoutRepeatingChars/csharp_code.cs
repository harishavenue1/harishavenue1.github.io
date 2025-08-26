using System;
using System.Collections.Generic;

class Program {
    public static void Main() {
        int maxLength = LengthOfLongestSubstring("abcabcbb");
        Console.WriteLine($"max length {maxLength}");
    }
    
    public static int LengthOfLongestSubstring(string s) {
        int n = s.Length;  // C#: .Length property for strings (capital L)
        int maxLength = 0;

        // C#: Dictionary to store character -> last seen index mapping
        Dictionary<char, int> charMap = new Dictionary<char, int>();
        int left = 0;  // Left pointer of sliding window
        
        for (int right = 0; right < n; right++) {  // Right pointer expansion

            // C#: .ContainsKey() method to check if character exists
            if (!charMap.ContainsKey(s[right]) || charMap[s[right]] < left) {

                // Character not seen or outside current window
                maxLength = Math.Max(maxLength, right - left + 1);
            } else {

                // Character found in current window, move left pointer
                left = charMap[s[right]] + 1;
            }

            // C#: Dictionary indexer to store/update character index
            charMap[s[right]] = right;
        }
        
        return maxLength;
    }
}