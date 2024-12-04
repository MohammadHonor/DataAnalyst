def solve(ls,n):
    new_ls = filter(lambda v : len(v)>n , ls)
    print(list(new_ls))
solve(["jack","tomaj","a","bb"],2)
