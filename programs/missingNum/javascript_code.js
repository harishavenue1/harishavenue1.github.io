missingNum = function (nums) {
    
    // JavaScript: Get array length using .length property
    let arrLen = nums.length
    
    // JavaScript: Calculate expected sum using arithmetic series formula
    let expectedSum = ((arrLen * (arrLen + 1)) / 2)
    
    // JavaScript: .reduce() method to calculate actual sum
    let actualSum = (nums).reduce((a, b) => (a + b))
    
    
    // JavaScript: Missing number is difference between expected and actual
    return expectedSum - actualSum
};

let arr = [3, 0, 1]
let miss_num = missingNum(arr)
console.log('Missing Number is', miss_num)

arr = [0, 1]
miss_num = missingNum(arr)
console.log('Missing Number is', miss_num)

arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
miss_num = missingNum(arr)
console.log('Missing Number is', miss_num)