function returnDistinctElements(arr) {
    
    // JavaScript: Two-pointer technique for removing duplicates in-place
    // slow tracks unique elements, fast scans array
    let slow = 0, fast = 1;
    
    // JavaScript: while loop with .length property
    while (fast < arr.length) {
        
        if (arr[slow] != arr[fast]) {
            
            // Move to next position for unique element
            slow++;
            
            // Place unique element
            arr[slow] = arr[fast];
        }
        
        
        // Always move fast pointer
        fast++;
    }
    
    
    // JavaScript: .slice(start, end) method creates new array
    return arr.slice(0, slow + 1);
}

// Test
let arr = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9];
console.log("Returned distinct array is " + JSON.stringify(returnDistinctElements(arr)));