function lengthOfLongestSubstring(s) {
    
    // JavaScript: .length property for strings
    const n = s.length;
    let maxLength = 0;
    
    // JavaScript: Map object to store character -> last seen index mapping
    const charMap = new Map();
    
    // Left pointer of sliding window
    let left = 0;
    
    
    // JavaScript: Right pointer expansion
    for (let right = 0; right < n; right++) {
        
        // JavaScript: .has() method to check if character exists in Map
        if (!charMap.has(s[right]) || charMap.get(s[right]) < left) {
            
            // Character not seen or outside current window
            maxLength = Math.max(maxLength, right - left + 1);
        } else {
            
            // Character found in current window, move left pointer
            left = charMap.get(s[right]) + 1;
        }
        
        
        // JavaScript: .set() method to store/update character index
        charMap.set(s[right], right);
    }
    
    return maxLength;
}

// Test
const maxLength = lengthOfLongestSubstring("abcabcbb");
console.log(`max length ${maxLength}`);