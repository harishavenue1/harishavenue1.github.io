findMin_sorted_rotatedArray = function (nums) {
    
    // JavaScript: Binary search pointers for rotated array
    let leftIndex = 0;
    let rightIndex = nums.length - 1;
    let midIndex = 0;

    
    // JavaScript: Modified binary search to find minimum
    while (leftIndex < rightIndex - 1) {
        
        // JavaScript: Math.floor() for integer division
        midIndex = Math.floor((leftIndex + rightIndex) / 2);
        
        // JavaScript: Compare middle with right to determine which half to search
        if (nums[midIndex] < nums[rightIndex])
            rightIndex = midIndex;  // Minimum is in left half
        else
            leftIndex = midIndex;   // Minimum is in right half
    }

    
    // JavaScript: Ternary operator to return smaller element
    return (nums[leftIndex] < nums[rightIndex]) ? nums[leftIndex] : nums[rightIndex];
};

let arr = [3,4,5,1,2];
output = findMin_sorted_rotatedArray(arr);
console.log("Minimum of Sorted and if rotated Array is",output);

arr = [4,5,6,7,0,1,2]
output = findMin_sorted_rotatedArray(arr)
console.log("Minimum of Sorted and if rotated Array is",output);

arr = [11,13,15,17]
output = findMin_sorted_rotatedArray(arr)
console.log("Minimum of Sorted and if rotated Array is",output);
