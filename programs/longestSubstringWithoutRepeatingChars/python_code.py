def lengthOfLongestSubstring(s):
    
    # Python: len() function for string length
    n = len(s)
    max_length = 0
    
    # Python: Dictionary to store character -> last seen index mapping
    char_map = {}
    
    # Left pointer of sliding window
    left = 0
    
    
    # Python: range() for iteration, right pointer expansion
    for right in range(n):
        
        # Python: 'in' operator to check if character exists in dictionary
        if s[right] not in char_map or char_map[s[right]] < left:
            
            # Character not seen or outside current window
            max_length = max(max_length, right - left + 1)
        else:
            
            # Character found in current window, move left pointer
            left = char_map[s[right]] + 1
        
        # Python: Dictionary assignment to store/update character index
        char_map[s[right]] = right
    
    return max_length

if __name__ == "__main__":
    max_length = lengthOfLongestSubstring("abcabcbb")
    print(f"max length {max_length}")