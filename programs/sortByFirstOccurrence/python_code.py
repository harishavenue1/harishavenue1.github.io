def sort_by_first_occurrence():
    arr = [5,6,1,2,3,4,5,6,1,2,3]
    print("Initial List", arr)
    
    count_map = {}
    for i in arr:
        count_map[i] = count_map.get(i, 0) + 1
    
    new_list = []
    for k in count_map:
        for _ in range(count_map[k]):
            new_list.append(k)
    
    print("New List", new_list)
    return new_list

sort_by_first_occurrence()