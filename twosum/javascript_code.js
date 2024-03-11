var twoSum = function (nums, target) {
    const mp = {}

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i]

        if (diff in mp)
            return [i, mp[diff]]

        mp[nums[i]] = i
    }
}

console.log(twoSum([1, 2, 3, 4, 5], 9))