def topDown(src,dest,i,j,ind):
    if i==len(src) or j==len(dest):
        return 0
    if ind[i]>=j:
        m= max(topDown(src,dest,i+1,ind[i]+1,ind)+1,topDown(src,dest,i+1,j,ind))
    else:
        m= topDown(src,dest,i+1,j,ind)

    print(i,j,m)
    return m

def bottomUp(src,dest,ind):
    tab=[ [0 for i in range(len(src)+1)] for j in range(len(dest)+1)]
    for i in range(len(src)-1,-1,-1):
        for j in range(len(dest)-1,-1,-1):
            if ind[i]>=j:
                tab[i][j]=max(tab[i+1][ind[i]+1]+1,tab[i+1][j])
            else:
                tab[i][j]=tab[i+1][j]

    return tab[0][0]

li=list(map(int,input().split()))
li2=list(map(int,input().split()))
ind=[ 0 for i in range(max(li))]
for i in range(len(li)):
    ind[i]=li2.index(li[i])

print(bottomUp(li,li2,ind))


