function groupAnagrams(strs) {
    
    // JavaScript: Map object to group anagrams by sorted character key
    const map = new Map();
    
    
    // JavaScript: for-of loop for array iteration
    for (let str of strs) {
        
        // JavaScript: .split('') -> .sort() -> .join('') chain for sorting characters
        const key = str.split('').sort().join('');
        
        
        // JavaScript: .has() checks if key exists, .set() creates empty array
        if (!map.has(key)) {
            map.set(key, []);
        }
        
        // JavaScript: .get() retrieves array, .push() adds element
        map.get(key).push(str);
    }
    
    
    // JavaScript: Array.from() converts Map values to array
    return Array.from(map.values());
}