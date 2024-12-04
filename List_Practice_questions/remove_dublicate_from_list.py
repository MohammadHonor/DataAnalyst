def solve():
    # remove dublicate from the list 
    user_list = [1,1,2,2,2,3,3]
    frequence ={}
    for v in user_list:
        if v not in frequence:
            frequence[v]=1
        else :
            frequence[v]+=1
    # print(frequence)
    for k,v in frequence.items():
        # print(k)
        while v>1 :
            # print(k)
            user_list.remove(k)
            v-=1
    print(user_list)
solve()