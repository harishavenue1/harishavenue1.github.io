def mergeSortedArrays(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    
    arr3 = [0] * (len1 + len2)
    len3 = len(arr3)
    
    i, j, k = 0, 0, 0
    
    while(i<len1 and j<len2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i+=1
        else:
            arr3[k] = arr2[j]
            j+=1
        k+=1
        
    while(i<len1 and k<len3):
        arr3[k] = arr1[i]
        k+=1
        i+=1

    while(j<len2 and k<len3):
        arr3[k] = arr2[j]
        k+=1
        i+=1

    return arr3

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8] 
arr3 = mergeSortedArrays(arr1, arr2)
print("Merged Array", arr3)