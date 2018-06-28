def topDown(li,ind,m):
    if ind==len(li):
        return 0

    if li[ind]>m:
        return max(topDown(li,ind+1,li[ind])+1,topDown(li,ind+1,m))
    else:
        return topDown(li,ind+1,m)

def bottomUp(li):
    tab=[1 for n in range(len(li))]
    for i in range(1,len(li)):
        for j in range(i):
            if li[i]>li[j] and tab[i]<tab[j]+1:
                tab[i]=tab[j]+1


    return tab[-1]






li = list(map(int,input().split()))

print(bottomUp(li))
