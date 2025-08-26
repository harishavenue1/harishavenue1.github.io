mergeSortedArrays = function (arr1, arr2) {
    
    // JavaScript: Get array lengths using .length property
    len1 = arr1.length;
    len2 = arr2.length;

    
    // JavaScript: Create result array with new Array()
    arr3 = new Array(len1 + len2)
    len3 = arr3.length;

    
    // JavaScript: Three pointers for merging
    i = 0
    j = 0
    k = 0

    
    // JavaScript: Merge while both arrays have elements
    while (i < len1 && j < len2) {
        
        // JavaScript: Compare and add smaller element
        if (arr1[i] < arr2[j]) {
            arr3[k++] = arr1[i++]
        }
        else {
            arr3[k++] = arr2[j++]
        }
    }

    
    // JavaScript: Add remaining elements from first array
    while (i < len1 && k < len3) {
        arr3[k++] = arr1[i++]
    }

    
    // JavaScript: Add remaining elements from second array
    while (j < len2 && k < len3) {
        arr3[k++] = arr2[j++]
    }
    
    return arr3
};

let arr1 = [1, 3, 5, 7]
let arr2 = [2, 4, 6, 8]
arr3 = mergeSortedArrays(arr1, arr2)
console.log("Merged Array", arr3)