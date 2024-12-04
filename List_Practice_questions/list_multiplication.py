def multiply():
    # list
    user_string = input("Enter element of list seperated by space : ")
    user_list = user_string.split(" ")
    product = 1
    for v in user_list :
        product *= int(v)
    print(product)

multiply()