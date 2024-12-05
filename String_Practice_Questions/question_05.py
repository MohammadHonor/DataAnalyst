"""
5. Write a Python program to get a single string from two given strings, separated  
by a space and swap the first two characters of each string.   
Sample String : 'abc', 'xyz'  
Expected Result : 'xyc abz'
"""

def solve(s1,s2):
    temp1 = s1[len(s1)-1]
    temp2 = s2[len(s2)-1]

    return s2[0:len(s2)-1] + temp1 +" " + s1[0:len(s1)-1] + temp2
print(solve("abc" , "xyz"))
