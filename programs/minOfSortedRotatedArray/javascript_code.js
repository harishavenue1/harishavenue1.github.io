findMin_sorted_rotatedArray = function (nums) {
    let leftIndex = 0;
    let rightIndex = nums.length - 1;
    let midIndex = 0;

    while (leftIndex < rightIndex - 1) {
        midIndex = Math.floor((leftIndex + rightIndex) / 2);
        if (nums[midIndex] < nums[rightIndex])
            rightIndex = midIndex;
        else
            leftIndex = midIndex;
    }

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
