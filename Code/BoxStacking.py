def bottomUp(li):
    dim=[]
    for i in li:
        mp0=(i[0],i[1],i[2])
        mp1=(i[1],i[2],i[0])
        mp2=(i[0],i[2],i[1])
        dim.append(mp0)
        dim.append(mp1)
        dim.append(mp2)

    print(li)

    dim.sort(key = lambda x:x[0]*x[1])
    print(dim)
    tab=[ 0 for i in range(len(dim))]
    tab[-1]=dim[-1][2]

    for i in range(len(dim)-2,-1,-1):
        fl=0
        m=0
        for j in range(i+1,len(dim)):
            if ( dim[i][0]<dim[j][0] and dim[i][1]<dim[j][1] ) or (dim[i][0]<dim[j][1] and dim[i][1]<dim[j][0]):
                fl=1
                m=max(m,tab[j])
        if fl==1:
            tab[i]=m+dim[i][2]

        else:
            tab[i]=dim[i][2]


    return tab[0]

n = int(input())
li=[]
for i in range(n):
    l=tuple(map(int,input().split()))
    li.append(l)
print(bottomUp(li))




