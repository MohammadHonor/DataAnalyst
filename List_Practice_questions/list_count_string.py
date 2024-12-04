def count():
    # user_input = input("Enter list item as mix of string and number seperatated by commas :")
    # use_list = user_input.split(",")
    user_list = ["ali","b",1,2,4,"jack","j"]
    count = 0
    for v in user_list:
        if type(v) is str :
            count+=1
        # print(type(v))
    print(count)
count()