def topDown(mat,i,j):

    if i+1==len(mat) and j+1==len(mat[0]):
        return mat[i][j];

    if i+1==len(mat):
        return mat[i][j]+topDown(mat,i,j+1)
    elif j+1==len(mat[0]):
        return mat[i][j]+topDown(mat,i+1,j)

    return mat[i][j]+max(topDown(mat,i+1,j),topDown(mat,i,j+1))


def bottomUp(mat):
    table=mat
    for i in range(len(mat)-2,-1,-1):
        table[i][-1]=table[i][-1]+table[i+1][-1]
    for i in range(len(mat[0])-2,-1,-1):
        table[-1][i]=table[-1][i]+table[-1][i+1]

    for i in range(len(mat)-2,-1,-1):
        for j in range(len(mat[0])-2,-1,-1):
            table[i][j]+=max(table[i+1][j],table[i][j+1])


    return table[0][0]


n = int(input())
li=[]
for i in range(n):
    l=list(map(int,input().split()))
    li.append(l)

print(topDown(li,0,0))
print(bottomUp(li))


