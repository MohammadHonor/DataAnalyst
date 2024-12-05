"""
4. Write a Python program to get a string from a given string where all  
occurrences of its first char have been changed to '$', except the first char itself.   
Sample String : 'restart'  
Expected Result : 'resta$t
"""

def solve(s):
    temp = s[0]
    first = s[0]

    for i in range(1,len(s)) :
        if s[i] == first :
            temp += "$"
        else:
            temp +=s[i]
    return temp

use_input = input("Enter a String : ")
print(solve(use_input))


