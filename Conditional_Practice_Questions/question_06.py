#  Write a Python program to count the number of even and odd numbers from a  
# series of numbers.   
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

number = (1,2,3,4,5,6,7,8,9)
odd_count = 0
even_count = 0
for v in number:
    if v %2 != 0 :
        odd_count+=1
    else:
        even_count+=1
print(f"even count is {even_count} and odd count is {odd_count}")