function firstUniqueChar() {
    const s = "HarishHaresh";
    
    // way1 - count occurrences
    const map = new Map();
    for (const c of s) {
        map.set(c, (map.get(c) || 0) + 1);
    }
    
    for (const [k, count] of map) {
        if (count === 1) {
            console.log("First Unique Char is ->", k);
            break;
        }
    }
    
    // way2 - add/remove approach
    const set = new Set();
    const order = [];
    
    for (const c of s) {
        if (set.has(c)) {
            set.delete(c);
            const index = order.indexOf(c);
            if (index > -1) order.splice(index, 1);
        } else {
            set.add(c);
            order.push(c);
        }
    }
    
    if (set.size === 0) {
        console.log("There are no Unique Chars");
    } else {
        const firstUnique = order.find(c => set.has(c));
        console.log("First Unique Char is ->", firstUnique);
    }
}

firstUniqueChar();