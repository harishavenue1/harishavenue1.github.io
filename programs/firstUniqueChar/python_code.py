def first_unique_char():
    s = "HarishHaresh"
    
    # way1 - count occurrences
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    
    for k in char_count:
        if char_count[k] == 1:
            print("First Unique Char is ->", k)
            break
    
    # way2 - add/remove approach
    unique_chars = set()
    order = []
    
    for c in s:
        if c in unique_chars:
            unique_chars.remove(c)
            if c in order:
                order.remove(c)
        else:
            unique_chars.add(c)
            order.append(c)
    
    if len(unique_chars) == 0:
        print("There are no Unique Chars")
    else:
        first_unique = next(c for c in order if c in unique_chars)
        print("First Unique Char is ->", first_unique)

first_unique_char()