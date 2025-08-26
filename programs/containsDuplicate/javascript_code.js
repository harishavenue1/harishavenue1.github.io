containsDuplicate = function(nums) {
  
  // JavaScript: Set constructor automatically removes duplicates
  const inSet = new Set(nums);
  
  
  // JavaScript: Compare Set size with original array length
  // If sizes differ, duplicates existed in original array
  return inSet.size != nums.length;
};

console.log('Contains Duplicate ' + containsDuplicate([1,2,3,1]))
console.log('Contains Duplicate ' + containsDuplicate([1,2,3,4]))
console.log('Contains Duplicate ' + containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
