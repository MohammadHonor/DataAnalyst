def count_str_first_equal_last():
    user_string = ['abc', 'xyz', 'aba', '1221']
    count = 0
    for v in user_string :
        if v[0] == v[len(v)-1]:
            count +=1
    print(count)

count_str_first_equal_last()