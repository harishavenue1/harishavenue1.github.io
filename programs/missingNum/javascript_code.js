missingNum = function (nums) {
    let arrLen = nums.length
    let expectedSum = ((arrLen * (arrLen + 1)) / 2)
    let actualSum = (nums).reduce((a, b) => (a + b))
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