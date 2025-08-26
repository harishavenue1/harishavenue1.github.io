function topKFrequent(nums, k) {
    
    // JavaScript: Map to count frequency of each number
    const count = new Map();
    
    
    // JavaScript: for-of loop for array iteration
    for (let num of nums) {
        
        // JavaScript: .get() with || operator for default value
        count.set(num, (count.get(num) || 0) + 1);
    }
    
    
    // JavaScript: Array.from() converts Map keys to array
    return Array.from(count.keys())
        
        // JavaScript: .sort() with custom comparator function
        .sort((a, b) => count.get(b) - count.get(a))
        
        // JavaScript: .slice() gets first k elements
        .slice(0, k);
}