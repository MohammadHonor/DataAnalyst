def solve():
    user_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
    # output = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
    last_element =[]
    for v in user_list:
        last_element.append(v[len(v)-1])
        # print(type(v))
    last_element.sort()
    # print(last_element)
    sorted_element =[]
    for v in last_element:
        for tup in user_list:
            if v == tup[len(tup)-1] :
                sorted_element.append(tup)
    print(sorted_element)
solve()