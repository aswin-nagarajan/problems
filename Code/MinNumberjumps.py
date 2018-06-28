def bottomUp(li):
    tab= [0 for i in range(len(li))]
    for i in range(len(li)-2,-1,-1):
        m=float('Inf')
        for j in range(i+1,min(len(li),i+1+li[i])):
            m=min(m,tab[j])
        tab[i]=m+1
    print(tab)
    return tab[0]

li = list(map(int,input().split()))
print(bottomUp(li))

