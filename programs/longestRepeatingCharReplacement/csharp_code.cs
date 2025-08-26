using System;
using System.Collections.Generic;

public class Program {
    public static void Main() {
        int maxLen = CharacterReplacement("AABABBA", 2);
        Console.WriteLine($"Max length {maxLen}");
    }
    
    public static int CharacterReplacement(string s, int k) {
        
        // C#: Dictionary<TKey, TValue> for character frequency mapping
        Dictionary<char, int> charFreq = new Dictionary<char, int>();
        int start = 0;
        int windowSize = 0;
        int mostFreqCount = 0;
        
        
        // C#: .Length property (capital L)
        for (int i = 0; i < s.Length; i++) {
            
            // C#: Direct indexing s[i]
            char c = s[i];
            
            // C#: .GetValueOrDefault() method for default values
            charFreq[c] = charFreq.GetValueOrDefault(c, 0) + 1;
            
            // C#: Math.Max() static method
            mostFreqCount = Math.Max(mostFreqCount, charFreq[c]);
            
            
            // Sliding window: shrink if window invalid (too many replacements needed)
            if (windowSize + 1 > mostFreqCount + k) {
                
                // C#: -- decrement operator
                charFreq[s[start]]--;
                
                // Move window start
                start++;
            } else {
                
                // Expand window
                windowSize++;
            }
        }
        
        return windowSize;
    }
}