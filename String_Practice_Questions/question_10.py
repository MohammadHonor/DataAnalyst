def exchange_first_last_char_of_string():
    user_string = input("Enter a string : ")
    new_str = ""
    first_char = user_string[0]
    last_char = user_string[len(user_string)-1]
    new_str += last_char + user_string[1:len(user_string)-2] + first_char
    print(f"Ater exchanging first and last char : {new_str}")
exchange_first_last_char_of_string()