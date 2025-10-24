function sortByFirstOccurrence() {
    const arr = [5,6,1,2,3,4,5,6,1,2,3];
    console.log("Initial List", arr);
    
    const map = new Map();
    for(const i of arr) {
        map.set(i, (map.get(i) || 0) + 1);
    }
    
    const newArr = [];
    for(const [k, count] of map) {
        for(let v = 0; v < count; v++) {
            newArr.push(k);
        }
    }
    console.log("New List", newArr);
    return newArr;
}

sortByFirstOccurrence();