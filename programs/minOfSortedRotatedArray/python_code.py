def findMin_sorted_rotatedArray(nums):
    leftIndex, rightIndex = 0, len(nums) - 1
    midIndex = 0

    while (leftIndex < rightIndex - 1):
        midIndex = (leftIndex + rightIndex) // 2
        if (nums[midIndex] < nums[rightIndex]):
            rightIndex = midIndex
        else:
            leftIndex = midIndex

    return nums[leftIndex] if nums[leftIndex] < nums[rightIndex] else nums[rightIndex]

arr = [3,4,5,1,2]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)

arr = [4,5,6,7,0,1,2]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)

arr = [11,13,15,17]
output = findMin_sorted_rotatedArray(arr)
print("Minimum of Sorted and if rotated Array is",output)
