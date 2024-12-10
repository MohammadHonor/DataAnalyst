"""
Write a Python program to guess a number between 1 to 9.   
Note : User is prompted to enter a guess. If the user guesses wrong then the  
prompt appears again until the guess is correct, on successful guess, user will  
get a "Well guessed!" message, and the program will exit.  
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

def pattern():
    n = int(input("Enter a number"))
    for i in range(1,n+1):
        print(i*"* ")
    for j in range(n-1,0,-1):
        print(j*"* ")
pattern()