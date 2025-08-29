// Create and initialize Map
let fruits = new Map([
    ["apple", 5],
    ["banana", 3],
    ["cherry", 8]
]);
console.log("Initial map:", Array.from(fruits.entries()));

// Set operations
fruits.set("apple", 10); // Update existing
fruits.set("grape", 6); // Add new
console.log("After setting:", Array.from(fruits.entries()));

// Get operations
console.log("Apple count:", fruits.get("apple"));
console.log("Kiwi count:", fruits.get("kiwi") || 0);

// Check operations
console.log("Has apple:", fruits.has("apple"));
console.log("Size:", fruits.size);
console.log("Is empty:", fruits.size === 0);

// Iteration methods
console.log("Keys:", Array.from(fruits.keys()));
console.log("Values:", Array.from(fruits.values()));
console.log("Entries:", Array.from(fruits.entries()));

// Iterate using forEach
console.log("forEach iteration:");
fruits.forEach((value, key) => {
    console.log(`  ${key} = ${value}`);
});

// Iterate using for...of
console.log("for...of iteration:");
for (let [key, value] of fruits) {
    console.log(`  ${key} -> ${value}`);
}

// Create Object (alternative to Map)
let fruitsObj = {
    apple: 5,
    banana: 3,
    cherry: 8
};
console.log("Object version:", fruitsObj);

// Object operations
fruitsObj.grape = 6; // Add new
fruitsObj["mango"] = 4; // Add using bracket notation
console.log("After adding to object:", fruitsObj);

// Object methods
console.log("Object keys:", Object.keys(fruitsObj));
console.log("Object values:", Object.values(fruitsObj));
console.log("Object entries:", Object.entries(fruitsObj));

// Check in object
console.log("Object has apple:", "apple" in fruitsObj);
console.log("Object has apple (hasOwnProperty):", fruitsObj.hasOwnProperty("apple"));

// Convert between Map and Object
let mapFromObject = new Map(Object.entries(fruitsObj));
console.log("Map from Object:", Array.from(mapFromObject.entries()));

let objectFromMap = Object.fromEntries(fruits);
console.log("Object from Map:", objectFromMap);

// Filter and transform
let highValueFruits = new Map(
    Array.from(fruits.entries()).filter(([key, value]) => value > 5)
);
console.log("High value fruits:", Array.from(highValueFruits.entries()));

// Update values
fruits.forEach((value, key) => {
    if (value < 10) {
        fruits.set(key, value + 1);
    }
});
console.log("After incrementing low values:", Array.from(fruits.entries()));

// Merge Maps
let citrus = new Map([
    ["orange", 12],
    ["lemon", 3],
    ["lime", 5]
]);

let combined = new Map([...fruits, ...citrus]);
console.log("Combined maps:", Array.from(combined.entries()));

// Remove operations
fruits.delete("banana");
console.log("After deleting banana:", Array.from(fruits.entries()));

// Clear map
fruits.clear();
console.log("After clear:", Array.from(fruits.entries()));

// WeakMap example (keys must be objects)
let weakMap = new WeakMap();
let obj1 = {name: "apple"};
let obj2 = {name: "banana"};

weakMap.set(obj1, 5);
weakMap.set(obj2, 3);
console.log("WeakMap has obj1:", weakMap.has(obj1));
console.log("WeakMap get obj1:", weakMap.get(obj1));