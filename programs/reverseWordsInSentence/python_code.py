def reverse_words_in_sentence():
    s = "your code goes here"
    s_arr = s.split(" ")
    
    # way1 - using slicing
    for i in range(len(s_arr)):
        s_arr[i] = s_arr[i][::-1]
    print("Final String reversed is", s_arr)
    
    # way2 - manual reversal
    s_arr = s.split(" ")
    for i in range(len(s_arr)):
        word = s_arr[i]
        new_word = ""
        for j in range(len(word) - 1, -1, -1):
            new_word += word[j]
        s_arr[i] = new_word
    print("Final String reversed is", s_arr)
    return s_arr

reverse_words_in_sentence()