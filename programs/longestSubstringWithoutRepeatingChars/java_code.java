import java.util.HashMap;
import java.util.Map;

class java_code {
    public static void main(String[] args) {
        int maxLength = lengthOfLongestSubstring("abcabcbb");
        System.out.println("max length " + maxLength);
    }

    public static int lengthOfLongestSubstring(String s) {
        
        // Java: .length() method for strings
        int n = s.length();
        int maxLength = 0;
        
        // Java: HashMap to store character -> last seen index mapping
        Map<Character, Integer> charMap = new HashMap<>();
        
        // Left pointer of sliding window
        int left = 0;

        
        // Right pointer expansion
        for (int right = 0; right < n; right++) {
            
            // Java: .containsKey() to check if character exists in map
            if (!charMap.containsKey(s.charAt(right)) || charMap.get(s.charAt(right)) < left) {
                
                // Character not seen or outside current window
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                
                // Character found in current window, move left pointer
                left = charMap.get(s.charAt(right)) + 1;
            }
            
            // Java: .put() to store/update character index
            charMap.put(s.charAt(right), right);
        }
        return maxLength;
    }
}