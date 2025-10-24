function divisibilityCheck() {
    const num = 64;
    console.log("Number:", num);
    
    // Traditional modulo approach
    if (num % 32 === 0) {
        console.log("abc");
    } else if (num % 16 === 0) {
        console.log("b");
    } else if (num % 8 === 0) {
        console.log("a");
    } else {
        console.log("none");
    }
    
    // Bitwise approach (tricky interview method)
    console.log("\nBitwise approach:");
    if ((num & 31) === 0) {
        console.log("abc");
    } else if ((num & 15) === 0) {
        console.log("b");
    } else if ((num & 7) === 0) {
        console.log("a");
    } else {
        console.log("none");
    }
}

divisibilityCheck();