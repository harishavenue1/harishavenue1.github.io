import java.util.HashMap;
import java.util.Map;

class java_code {
    public static void main(String[] args) {
        int maxLength = lengthOfLongestSubstring("abcabcbb");
        System.out.println("max length " + maxLength);
    }

    public static int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        Map<Character, Integer> charMap = new HashMap<>();
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (!charMap.containsKey(s.charAt(right)) || charMap.get(s.charAt(right)) < left) {
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                left = charMap.get(s.charAt(right)) + 1;
            }
            charMap.put(s.charAt(right), right);
        }
        return maxLength;
    }
}