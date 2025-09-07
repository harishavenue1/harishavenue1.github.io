import java.util.HashMap;
import java.util.Map;

public class java_code {
    public static void main(String[] args) {
        String s = "AABABBA";
        int k = 2;
        System.out.println("String: \"" + s + "\"");
        System.out.println("Max replacements allowed: " + k);
        
        int maxLen = characterReplacement(s, k);
        System.out.println("\n=== FINAL RESULT: " + maxLen + " ===");
    }

    public static int characterReplacement(String s, int k) {
        System.out.println("\n=== LONGEST REPEATING CHARACTER REPLACEMENT ===");
        
        // Java: HashMap for character frequency mapping
        Map<Character, Integer> charFreq = new HashMap<>();
        int start = 0, windowSize = 0;
        int mostFreqCount = 0;

        // Java: .length() method for strings
        for (int i = 0; i < s.length(); i++) {
            // Java: .charAt() to access character at index
            char c = s.charAt(i);
            
            System.out.printf("\nStep %d: Processing char '%c' at index %d\n", i + 1, c, i);
            System.out.println("Current window: [" + start + ", " + i + "] = \"" + s.substring(start, i + 1) + "\"");
            System.out.println("CharFreq before: " + charFreq);

            // Java: .getOrDefault() provides default value if key not found
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
            System.out.println("CharFreq after adding '" + c + "': " + charFreq);

            // Java: Math.max() for maximum value
            int oldMostFreq = mostFreqCount;
            mostFreqCount = Math.max(mostFreqCount, charFreq.get(c));
            if (mostFreqCount > oldMostFreq) {
                System.out.println("✨ New most frequent count: " + oldMostFreq + " -> " + mostFreqCount);
            } else {
                System.out.println("Most frequent count remains: " + mostFreqCount);
            }
            
            int currentWindowLength = i - start + 1;
            int replacementsNeeded = currentWindowLength - mostFreqCount;
            System.out.println("Window length: " + currentWindowLength + ", Most freq: " + mostFreqCount + ", Replacements needed: " + replacementsNeeded);

            // Sliding window: shrink if window invalid (too many replacements needed)
            if (replacementsNeeded > k) {
                char leftChar = s.charAt(start);
                System.out.println("❌ Too many replacements needed (" + replacementsNeeded + " > " + k + "). Shrinking window.");
                System.out.println("Removing '" + leftChar + "' from position " + start);
                
                charFreq.put(leftChar, charFreq.get(leftChar) - 1);
                if (charFreq.get(leftChar) == 0) {
                    charFreq.remove(leftChar);
                }
                
                // Move window start
                start++;
                System.out.println("New window start: " + start);
                System.out.println("CharFreq after removal: " + charFreq);
            } else {
                // Expand window
                windowSize++;
                System.out.println("✅ Valid window. Expanding window size to: " + windowSize);
            }
            
            System.out.println("Current max window size: " + windowSize);
        }
        return windowSize;
    }
}
