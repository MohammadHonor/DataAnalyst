import copy
def clone():
    ls = [1,2,3,4]
    # new_ls =ls.copy()
    new_ls =copy.copy(ls)
    print(new_ls)
clone()