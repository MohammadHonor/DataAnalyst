def smallestNumberOfList():
    user_string = input("Enter a list item seperated by commas : ")
    user_list = user_string.split(",")
    print(user_list)
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    smallest = float('inf')
    # print(large)
    for v in user_list:
        if v < smallest :
            smallest = v
    print(smallest)  

smallestNumberOfList()