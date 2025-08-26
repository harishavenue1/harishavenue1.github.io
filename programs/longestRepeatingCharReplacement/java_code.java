package programs.longestRepeatingCharReplacement;

import java.util.HashMap;
import java.util.Map;

public class java_code {
    public static void main(String[] args) {
        int maxLen = characterReplacement("AABABBA", 2);
        System.out.println("Max length " + maxLen);
    }

    public static int characterReplacement(String s, int k) {
        
        // Java: HashMap for character frequency mapping
        Map<Character, Integer> charFreq = new HashMap<>();
        int start = 0, windowSize = 0;
        int mostFreqCount = 0;

        
        // Java: .length() method for strings
        for (int i = 0; i < s.length(); i++) {
            
            // Java: .charAt() to access character at index
            char c = s.charAt(i);
            
            // Java: .getOrDefault() provides default value if key not found
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
            
            // Java: Math.max() for maximum value
            mostFreqCount = Math.max(mostFreqCount, charFreq.get(c));

            
            // Sliding window: shrink if window invalid (too many replacements needed)
            if (windowSize + 1 > mostFreqCount + k) {
                charFreq.put(s.charAt(start), charFreq.get(s.charAt(start)) - 1);
                
                // Move window start
                start++;
            } else
                
                // Expand window
                windowSize++;
        }
        return windowSize;
    }
}
