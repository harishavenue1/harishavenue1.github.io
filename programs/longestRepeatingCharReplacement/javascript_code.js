function characterReplacement(s, k) {
    
    // JavaScript: Map object for character frequency mapping
    const charFreq = new Map();
    let start = 0;
    let windowSize = 0;
    let mostFreqCount = 0;
    
    
    // JavaScript: .length property
    for (let i = 0; i < s.length; i++) {
        
        // JavaScript: Direct indexing s[i]
        const c = s[i];
        
        // JavaScript: .get() with || operator for default value
        charFreq.set(c, (charFreq.get(c) || 0) + 1);
        
        // JavaScript: Math.max() static method
        mostFreqCount = Math.max(mostFreqCount, charFreq.get(c));
        
        
        // Sliding window: shrink if window invalid (too many replacements needed)
        if (windowSize + 1 > mostFreqCount + k) {
            charFreq.set(s[start], charFreq.get(s[start]) - 1);
            
            // Move window start
            start++;
        } else {
            
            // Expand window
            windowSize++;
        }
    }
    
    return windowSize;
}

// Test
const maxLen = characterReplacement("AABABBA", 2);
console.log(`Max length ${maxLen}`);