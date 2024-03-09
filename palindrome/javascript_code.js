function isPalindrome(str) {
    const reversed = str.split('').reverse().join('');
    return str === reversed;
}

const str = "radar";
if (isPalindrome(str)) {
    console.log(str + " is a palindrome.");
} else {
    console.log(str + " is not a palindrome.");
}
