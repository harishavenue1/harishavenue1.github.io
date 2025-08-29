// Create and initialize sets
let fruits = new Set(["apple", "banana", "cherry"]);
fruits.add("apple"); // Duplicate - won't be added
console.log("Initial set:", Array.from(fruits));

// Add operations
["grape", "mango", "banana"].forEach(fruit => fruits.add(fruit));
console.log("After adding:", Array.from(fruits));

// Check operations
console.log("Contains apple:", fruits.has("apple"));
console.log("Size:", fruits.size);
console.log("Is empty:", fruits.size === 0);

// Create second set for operations
let citrus = new Set(["orange", "lemon", "grape"]);
console.log("Citrus set:", Array.from(citrus));

// Set operations - Union
let union = new Set([...fruits, ...citrus]);
console.log("Union:", Array.from(union));

// Set operations - Intersection
let intersection = new Set([...fruits].filter(x => citrus.has(x)));
console.log("Intersection:", Array.from(intersection));

// Set operations - Difference
let difference = new Set([...fruits].filter(x => !citrus.has(x)));
console.log("Difference (fruits - citrus):", Array.from(difference));

// Set operations - Symmetric Difference
let symDiff = new Set([
    ...[...fruits].filter(x => !citrus.has(x)),
    ...[...citrus].filter(x => !fruits.has(x))
]);
console.log("Symmetric Difference:", Array.from(symDiff));

// Check subset/superset
let subset = new Set(["apple", "banana"]);
let isSubset = [...subset].every(x => fruits.has(x));
let isSuperset = [...fruits].every(x => subset.has(x)) && fruits.size >= subset.size;
console.log("Is subset:", isSubset);
console.log("Is superset of subset:", [...subset].every(x => fruits.has(x)));

// Convert to array
let fruitsArray = Array.from(fruits);
console.log("Set to Array:", fruitsArray);

// Convert to array using spread
let fruitsSpread = [...fruits];
console.log("Set to Array (spread):", fruitsSpread);

// Check overlaps
let hasOverlap = [...fruits].some(x => citrus.has(x));
console.log("Overlaps with citrus:", hasOverlap);

// Iterate through set
console.log("Iteration using forEach:");
fruits.forEach(fruit => console.log("  " + fruit));

// Iterate using for...of
console.log("Iteration using for...of:");
for (let fruit of fruits) {
    console.log("  " + fruit);
}

// Remove operations
fruits.delete("banana");
console.log("After removing banana:", Array.from(fruits));

// Clear set
fruits.clear();
console.log("After clear:", Array.from(fruits));