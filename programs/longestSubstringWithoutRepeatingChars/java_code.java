import java.util.HashMap;
import java.util.Map;

class java_code {
    public static void main(String[] args) {
        System.out.println("=== STARTING LONGEST SUBSTRING ALGORITHM ===");
        String testString = "abcabcfbb";
        System.out.println("Input string: \"" + testString + "\"");
        System.out.println("String length: " + testString.length());

        int maxLength = lengthOfLongestSubstring(testString);
        System.out.println("\n=== ALGORITHM COMPLETED ===");
        System.out.println("Final result: " + maxLength);
    }

    public static int lengthOfLongestSubstring(String s) {
        int left = 0, maxLen = 0;
        char c;
        Map<Character, Integer> map = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            c = s.charAt(right);

            // if the character is not in the map or its index is less than the left pointer
            // - its a new character
            if (!map.containsKey(c) || map.get(c) < left) {
                maxLen = Math.max(maxLen, right - left + 1);
            }

            // otherwise, we found a repeating character, so we move the left pointer using
            // index of the repeating character + 1
            else {
                left = map.get(c) + 1;
            }
            map.put(c, right);
        }

        return maxLen;
    }
}