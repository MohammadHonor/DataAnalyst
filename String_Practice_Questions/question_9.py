def remove_nth_index_char(n):
    user_str = input("Enter a string : ")
    new_str = ""
    if n > len(user_str) :
        return f"Not possible to remove {n} index"
    else :
        for i in range(len(user_str)):
            if i != n :
                new_str += user_str[i]
        return f"after remove index {n} the new str is {new_str}"
index = int(input("Enter your index to remove the char assuming zero based indexing: "))
print(remove_nth_index_char(index))
