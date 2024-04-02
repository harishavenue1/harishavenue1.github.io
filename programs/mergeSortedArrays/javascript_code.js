mergeSortedArrays = function (arr1, arr2) {
    len1 = arr1.length;
    len2 = arr2.length;

    arr3 = new Array(len1 + len2)
    len3 = arr3.length;

    i = 0
    j = 0
    k = 0

    while (i < len1 && j < len2) {
        if (arr1[i] < arr2[j]) {
            arr3[k++] = arr1[i++]
        }
        else {
            arr3[k++] = arr2[j++]
        }
    }

    while (i < len1 && k < len3) {
        arr3[k++] = arr1[i++]
    }

    while (j < len2 && k < len3) {
        arr3[k++] = arr2[j++]
    }
    return arr3
};

let arr1 = [1, 3, 5, 7]
let arr2 = [2, 4, 6, 8]
arr3 = mergeSortedArrays(arr1, arr2)
console.log("Merged Array", arr3)