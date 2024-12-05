def solve(s):
    """
    Write a Python program to add 'ing' at the end of a given string (length should  
    be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the  
    string length of the given string is less than 3, leave it unchanged.   
    Sample String : 'abc'  
    """
    if len(s) <=3 and "ing" not in s:
        return s+"ing"
    elif "ing" in s :
        return s + "ly"
    else :
        return s
user_str = input("Enter a string : ")
print(solve(user_str))



