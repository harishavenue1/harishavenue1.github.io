function replacedString1(str) {
    
    // JavaScript: .split('') -> .map() -> .join('') chain for character transformation
    return str.split('').map(c => c === 'o' ? '&' : c).join('');
}

function replacedString2(str) {
    let count = 1;
    
    // JavaScript: Array to collect results
    let result = [];
    
    // JavaScript: for-of loop for string iteration
    for (let c of str) {
        if (c === 'o') {
            
            // JavaScript: Array.from() with length and mapping function to generate sequence
            result.push(Array.from({length: count}, (_, i) => i + 1).join(''));
            count++;
        } else {
            
            // JavaScript: .push() adds to array
            result.push(c);
        }
    }
    
    // JavaScript: .join('') concatenates array elements
    return result.join('');
}

function replacedString3(str) {
    let count = 1;
    
    // JavaScript: .split('') -> .map() -> .join('') with closure variable
    return str.split('').map(c => {
        
        // JavaScript: .toLowerCase() for case-insensitive comparison
        if (c.toLowerCase() === 'o') {
            
            // JavaScript: .repeat() method for string repetition
            return '&'.repeat(count++);
        }
        return c;
    }).join('');
}

// Test
const str = "tomorrow";
console.log(`Replaced String ${replacedString1(str)}`);
console.log(`Replaced String ${replacedString2(str)}`);
console.log(`Replaced String ${replacedString3(str)}`);