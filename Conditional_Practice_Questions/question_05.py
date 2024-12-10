"""
Write a Python program that accepts a word from the user and reverse it.   
"""

def reverse(word):
    word_list = list(word)
    first = 0 
    last = len(word_list)-1
    while(first < last ):
        temp = word_list[first]
        word_list[first]=word_list[last]
        word_list[last]=temp
        first+=1
        last-=1
    reverse_word = ""
    for v in word_list:
        reverse_word+=v
    return reverse_word
print(reverse("ali"))