var twoSum = function (nums, target) {
    
    // JavaScript: Object {} to store number -> index mapping for O(1) lookup
    const mp = {}

    
    // JavaScript: Standard for-loop with .length property
    for (let i = 0; i < nums.length; i++) {
        
        // Calculate complement needed to reach target
        const diff = target - nums[i]

        
        // JavaScript: 'in' operator checks if complement exists in object
        if (diff in mp)
            
            // JavaScript: Array literal syntax for return
            return [i, mp[diff]]

        
        // JavaScript: Object property assignment
        mp[nums[i]] = i
    }
}

console.log(twoSum([1, 2, 3, 4, 5], 9))