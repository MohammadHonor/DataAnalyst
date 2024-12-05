""""3. Write a Python program to get a string made of the first 2 and the last 2 chars  
from a given a string. If the string length is less than 2, return instead of the  
empty string.   
Sample String : 'w3resource'  
Expected Result : 'w3ce'  
Sample String : 'w3'  
Expected Result : 'w3w3'  
Sample String : ' w'  
Expected Result : Empty String
"""

def solve(s):
    s = s.strip()
    print(s)
    new_str =""
    if len(s)<2 :
        return "Empty String"
    else :
        new_str += s[0:2] + s[len(s)-2:len(s)]
        return new_str
user_str = input("Enter a string : ")
print(solve(user_str))

