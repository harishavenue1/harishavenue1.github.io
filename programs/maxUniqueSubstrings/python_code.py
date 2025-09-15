def max_unique_substrings(s):
    """Find maximum number of unique substrings using backtracking"""
    def backtrack(start, used):
        if start == len(s):
            return 0
        
        max_count = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in used:
                used.add(substring)
                count = 1 + backtrack(end, used)
                max_count = max(max_count, count)
                used.remove(substring)
        
        return max_count
    
    return backtrack(0, set())