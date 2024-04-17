package programs.longestRepeatingCharReplacement;

import java.util.HashMap;
import java.util.Map;

public class java_code {
    public static void main(String[] args) {
        int maxLen = characterReplacement("AABABBA", 2);
        System.out.println("Max length " + maxLen);
    }

    public static int characterReplacement(String s, int k) {
        Map<Character, Integer> charFreq = new HashMap<>();
        int start = 0, windowSize = 0;
        int mostFreqCount = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
            mostFreqCount = Math.max(mostFreqCount, charFreq.get(c));

            if (windowSize + 1 > mostFreqCount + k) {
                charFreq.put(s.charAt(start), charFreq.get(s.charAt(start)) - 1);
                start++;
            } else
                windowSize++;
        }
        return windowSize;
    }
}
