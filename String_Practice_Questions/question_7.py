def string_formating(user_str ):
    user_str_word_list = user_str.split(" ")
    print(user_str_word_list)
    if 'not' in user_str_word_list and 'poor!' in user_str_word_list :
        not_index = user_str_word_list.index("not")
        poor_index = user_str_word_list.index("poor!")
        # print(not_index,poor_index)
        new_str = ""
        if not_index < poor_index :
            # for i in range(not_index , poor_index+1):
            #     print(user_str_word_list[i])
            #     user_str_word_list.remove(user_str_word_list[i])
            for i in range(len(user_str_word_list)) :
                if i <not_index or i > poor_index :
                    new_str += user_str_word_list[i]+" "
            return new_str+"good!"
        else :
            return user_str
    else :
        return user_str
user_str = input("Enter a sentence : ")
print(string_formating(user_str))