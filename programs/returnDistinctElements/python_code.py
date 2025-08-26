def returnDistinctElements(arr):

    # Two-pointer technique: slow tracks unique elements, fast scans array
    slow = 0
    fast = 1
    while fast < len(arr):  # Python: len() function for array length
        if arr[slow] != arr[fast]:
            slow += 1  # Move to next position for unique element
            arr[slow] = arr[fast]  # Place unique element
        fast += 1  # Always move fast pointer

    # Python: List slicing [start:end] creates new list
    return arr[0:slow+1]

if __name__ == "__main__":
    arr = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9]
    print("Returned distinct array is", returnDistinctElements(arr))