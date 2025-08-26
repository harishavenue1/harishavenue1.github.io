function isValid(s) {
    
    // JavaScript: Array [] used as stack (LIFO with push/pop)
    const stack = [];
    
    // JavaScript: Object literal for closing -> opening bracket mapping
    const map = { ')': '(', '}': '{', ']': '[' };
    
    
    // JavaScript: for-of loop for string iteration
    for (let char of s) {
        
        // JavaScript: 'in' operator to check if property exists in object
        if (char in map) {
            
            // JavaScript: .length property, .pop() removes last element
            if (stack.length === 0 || stack.pop() !== map[char]) {
                return false;
            }
        } else {
            
            // JavaScript: .push() adds to end of array (top of stack)
            stack.push(char);
        }
    }
    
    
    // JavaScript: Check if array is empty using .length
    return stack.length === 0;
}