function isPalindrome(str) {
    
    // JavaScript: Chain .split('') -> .reverse() -> .join('') to reverse string
    const reversed = str.split('').reverse().join('');
    
    // JavaScript: === for strict equality comparison
    return str === reversed;
}

const str = "radar";
if (isPalindrome(str)) {
    console.log(str + " is a palindrome.");
} else {
    console.log(str + " is not a palindrome.");
}
