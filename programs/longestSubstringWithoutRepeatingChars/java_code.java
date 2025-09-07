import java.util.HashMap;
import java.util.Map;

class java_code {
    public static void main(String[] args) {
        int maxLength = lengthOfLongestSubstring("abcabcfbb");
        System.out.println("max length " + maxLength);
    }

    public static int lengthOfLongestSubstring(String s) {
        System.out.println("\nDebugging string: \"" + s + "\"");
        
        // Java: .length() method for strings
        int n = s.length();
        int maxLength = 0;

        // Java: HashMap to store character -> last seen index mapping
        Map<Character, Integer> charMap = new HashMap<>();

        // Left pointer of sliding window
        int left = 0;

        // Right pointer expansion
        for (int right = 0; right < n; right++) {
            char currentChar = s.charAt(right);
            System.out.printf("\nStep %d: Processing char '%c' at index %d\n", right + 1, currentChar, right);
            System.out.println("Current window: [" + left + ", " + right + "] = \"" + s.substring(left, right + 1) + "\"");
            System.out.println("CharMap before: " + charMap);

            // Java: .containsKey() to check if character exists in map
            if (!charMap.containsKey(currentChar) || charMap.get(currentChar) < left) {
                // Character not seen or outside current window
                int newLength = right - left + 1;
                maxLength = Math.max(maxLength, newLength);
                System.out.println("✓ Character not in current window. Window length: " + newLength + ", Max so far: " + maxLength);
            } else {
                // Character found in current window, move left pointer
                int oldLeft = left;
                left = charMap.get(currentChar) + 1;
                System.out.println("✗ Duplicate found! Moving left from " + oldLeft + " to " + left);
            }

            // Java: .put() to store/update character index
            charMap.put(currentChar, right);
            System.out.println("CharMap after: " + charMap);
            System.out.println("Current max length: " + maxLength);
        }
        
        System.out.println("\n=== FINAL RESULT: " + maxLength + " ===");
        return maxLength;
    }
}