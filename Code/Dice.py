def topDown(n,f,ind,s):
    if s==0:
        return 1
    if ind==n:
        return 0
    m=0
    for i in range(f):
        m=m+topDown(n,f,ind+1,s-i-1)

    return m

def bottomUp(n,f,s):
    tab = [ [ 0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        tab[i][0]=1
    for i in range(n-1,-1,-1):
        k=0
        temps=0
        for j in range(1,s+1):
            if k==f:
                temps=temps-tab[i+1][j-f-1]+tab[i+1][j-1]
            else:
                temps+=tab[i+1][j-1]

            tab[i][j]=temps
            k=k+1

    print(tab)

    return tab[0][s]


li=list(map(int,input().split()))
print(topDown(li[0],li[1],0,li[2]))
