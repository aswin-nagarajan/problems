

def bottomUp(li):
    c=[0 for no in range(len(li))]
    c[0]=li[0]
    n_S=0
    for i in range(1,len(li)):
        n_S=max(li[i],li[i]+n_S)
        c[i]=max(c[i-1],n_S)
        # c[i],c[i+1])
    print(c)
    return c[-1]

def topDown(win,ind,li):

    if win>len(li):
        return 0

    if ind==len(li):
        return 0

    # print(win,ind)
    return max(sum(li[ind:ind+win]),topDown(win,ind+1,li),topDown(win+1,ind,li))





n= int(input())
for i in range(n):
    l= int(input())
    li = list(map(int, input().split()))
    s=0
    for a in li:
        if a>0:
            s+=a;

    sj = topDown(1,0,li)
    print(s,sj, end='\n')








