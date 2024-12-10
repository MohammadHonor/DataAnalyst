#  Write a Python program that prints each item and its corresponding type from  
# the following list.  
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'Python foundation', (0, -1), [5,  
# 12], {"class":'V', "section":'A'}]

def display_type_of_each(ls):
    for v in ls:
        print(f"The item is {v} and type is {type(v)}")
datalist = [1452, 11.23, 1+2j, True, 'Python foundation', (0, -1), [5,  
12], {"class":'V', "section":'A'}]        
display_type_of_each(datalist)