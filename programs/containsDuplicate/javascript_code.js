containsDuplicate = function(nums) {
  const inSet = new Set(nums);
  return inSet.size != nums.length; //set.has(value) will return boolean
};

console.log('Contains Duplicate ' + containsDuplicate([1,2,3,1]))
console.log('Contains Duplicate ' + containsDuplicate([1,2,3,4]))
console.log('Contains Duplicate ' + containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
