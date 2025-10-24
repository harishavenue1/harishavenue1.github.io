function reverseWordsInSentence() {
    const s = "your code goes here";
    let sArr = s.split(" ");
    
    // way1 - using built-in reverse
    for (let i = 0; i < sArr.length; i++) {
        sArr[i] = sArr[i].split("").reverse().join("");
    }
    console.log("Final String reversed is", sArr);
    
    // way2 - manual reversal
    sArr = s.split(" ");
    for (let i = 0; i < sArr.length; i++) {
        const str = sArr[i];
        let newStr = "";
        for (let j = str.length - 1; j >= 0; j--) {
            newStr += str[j];
        }
        sArr[i] = newStr;
    }
    console.log("Final String reversed is", sArr);
    return sArr;
}

reverseWordsInSentence();