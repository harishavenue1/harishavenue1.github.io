public class java_code {
    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "ace";
        
        System.out.println("String 1: \"" + s1 + "\"");
        System.out.println("String 2: \"" + s2 + "\"");
        
        int result = longestCommonSubsequence(s1, s2);
        System.out.println("\nLongest Common Subsequence Length: " + result);
    }

    // Simple approach - just scan and match characters
    public static int longestCommonSubsequence(String text1, String text2) {
        int count = 0;
        int j = 0; // Pointer for text2
        String matchedSequence = "";
        
        System.out.println("\n=== SIMPLE CHARACTER MATCHING ===");
        System.out.println("Algorithm: Scan text1, find each character in remaining text2");
        System.out.printf("Initial state: count=%d, text2_pointer=%d, matched_sequence=\"%s\"\n", count, j, matchedSequence);
        
        // Go through each character in text1
        for (int i = 0; i < text1.length(); i++) {
            char c1 = text1.charAt(i);
            System.out.printf("\n--- Step %d ---\n", i + 1);
            System.out.printf("Current character: text1[%d] = '%c'\n", i, c1);
            System.out.printf("Searching in text2 from position %d onwards: \"%s\"\n", j, 
                j < text2.length() ? text2.substring(j) : "(end of string)");
            
            boolean foundMatch = false;
            
            // Look for this character in remaining part of text2
            for (int k = j; k < text2.length(); k++) {
                char c2 = text2.charAt(k);
                System.out.printf("  [%d] Comparing '%c' with text2[%d]='%c'\n", k-j+1, c1, k, c2);
                
                if (c1 == c2) {
                    count++;
                    matchedSequence += c1;
                    j = k + 1; // Move past this character in text2
                    foundMatch = true;
                    System.out.printf("  ✅ MATCH! '%c' found at text2[%d]\n", c1, k);
                    System.out.printf("  📊 Updated: count=%d, matched_sequence=\"%s\", next_search_pos=%d\n", 
                        count, matchedSequence, j);
                    break;
                } else {
                    System.out.printf("  ❌ '%c' != '%c'\n", c1, c2);
                }
            }
            
            if (!foundMatch) {
                System.out.printf("  🚫 Character '%c' not found in remaining text2\n", c1);
            }
            
            System.out.printf("End of step %d: count=%d, matched=\"%s\", remaining_text2=\"%s\"\n", 
                i + 1, count, matchedSequence, 
                j < text2.length() ? text2.substring(j) : "(none)");
        }
        
        System.out.println("\n=== FINAL RESULTS ===");
        System.out.println("Longest Common Subsequence: \"" + matchedSequence + "\"");
        System.out.println("Total matches found: " + count);
        return count;
    }
}
