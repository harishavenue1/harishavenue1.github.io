def characterReplacement(s, k):
    
    # Python: Dictionary {} for character frequency mapping
    char_freq = {}
    start = 0
    window_size = 0
    most_freq_count = 0
    
    
    # Python: range() and len() for iteration
    for i in range(len(s)):
        
        # Python: Direct indexing s[i] to access character
        c = s[i]
        
        # Python: .get() method provides default value if key not found
        char_freq[c] = char_freq.get(c, 0) + 1
        
        # Python: Built-in max() function
        most_freq_count = max(most_freq_count, char_freq[c])
        
        
        # Sliding window: shrink if window invalid (too many replacements needed)
        if window_size + 1 > most_freq_count + k:
            
            # Python: -= operator for decrement
            char_freq[s[start]] -= 1
            
            # Move window start
            start += 1
        else:
            
            # Expand window
            window_size += 1
    
    return window_size

if __name__ == "__main__":
    max_len = characterReplacement("AABABBA", 2)
    print(f"Max length {max_len}")