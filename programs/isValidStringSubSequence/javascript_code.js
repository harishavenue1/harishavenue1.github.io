isValidSubSequence = function (s1, s2) {
    let m = s1.length
    let n = s2.length

    let j = 0
    for (let i = 0; i < n; i++) {
        if (s1[j] == s2[i])
            j = j + 1
    }
    return j == m
};

let str1 = 'gksr%ek@@@'
let str2 = 'geeksforge%eks@@@'
let isValid = isValidSubSequence(str1, str2)
console.log('Valid SubSequence', isValid)