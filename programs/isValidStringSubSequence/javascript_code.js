isValidSubSequence = function (s1, s2) {
    
    // JavaScript: Get string lengths using .length property
    let m = s1.length
    let n = s2.length

    
    // JavaScript: Pointer for subsequence string
    let j = 0
    
    // JavaScript: Standard for-loop
    for (let i = 0; i < n; i++) {
        
        // JavaScript: Direct character comparison using indexing
        if (s1[j] == s2[i])
            j = j + 1  // Move subsequence pointer forward
    }
    
    
    // JavaScript: Check if all characters of subsequence were found
    return j == m
};

let str1 = 'gksr%ek@@@'
let str2 = 'geeksforge%eks@@@'
let isValid = isValidSubSequence(str1, str2)
console.log('Valid SubSequence', isValid)