threeSumEqZero = function (nums) {
    let leftIndex = 0
    let rightIndex = nums.length - 1
    let sum = 0

    // sort
    nums.sort((a, b) => { return a - b })
    console.log("Sorted Array is ", nums)

    // list to capture all possible values
    valuesList = []

    // list to capture unique values
    valuesSet = new Set()

    for (let i = 0; i < nums.length; i++) {
        leftIndex = i + 1
        while (leftIndex < rightIndex) {
            sum = nums[i] + nums[leftIndex] + nums[rightIndex]
            if (sum > 0)
                rightIndex--
            else if (sum < 0)
                leftIndex++
            else {
                valuesSet.add([nums[i], nums[leftIndex], nums[rightIndex]])
                console.log("Set of Values Equals to Zero ", valuesSet)
                leftIndex++
                rightIndex--
            }
        }
    }
    return Array.from(valuesSet)
};


arr = [-1, 0, 1, 2, -1, -4]
output = threeSumEqZero(arr)
console.log("List of Values Equals to Zero ", output)