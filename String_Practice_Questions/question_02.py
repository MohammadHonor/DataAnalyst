"""2. Write a Python program to count the number of characters (character  
frequency) in a string.   
Sample String : google.com'  
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 
"""

def solve(s):
    frequency ={}
    for v in s :
        if v not in frequency :
            frequency[v]=1
        else:
            frequency[v]+=1
    return frequency
user_str = input("Enter a String ")

print(solve(user_str))