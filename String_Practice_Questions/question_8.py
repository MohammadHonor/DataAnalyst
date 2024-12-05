def find_largest_length_word(ls):
    largest = 0
    for word in ls :
        largest = max(len(word),largest)
    for word in ls :
        if(len(word) == largest):
            return word
word_list = input("Enter list of word seperated by space ").split(" ")

largest_word = find_largest_length_word(word_list)
print(f"The largest length of world is {largest_word}")