/**
 * Find maximum number of unique substrings using backtracking
 */
function maxUniqueSplit(s) {
    function backtrack(start, used) {
        if (start === s.length) {
            return 0;
        }
        
        let maxCount = 0;
        for (let end = start + 1; end <= s.length; end++) {
            const substring = s.substring(start, end);
            if (!used.has(substring)) {
                used.add(substring);
                const count = 1 + backtrack(end, used);
                maxCount = Math.max(maxCount, count);
                used.delete(substring);
            }
        }
        
        return maxCount;
    }
    
    return backtrack(0, new Set());
}