
n ={}


def mem(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    m=0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                c = memoized(matrix,i,j)
                if m<c:
                    m=c
    return m


def memoized(matrix,i,j):
    rows = len(matrix)
    cols = len(matrix[0])
    if i==rows or cols==j:
        return 0
    if not matrix[i][j]:
        return 0

    if (i,j) in n.keys():
        return n[(i,j)]

    else:
        a= min(memoized(matrix,i+1,j),memoized(matrix,i+1,j+1),memoized(matrix,i,j+1))+1
        n[(i,j)]=a
        return a


def bottomUp


nj=int(input("no. of rows"))
mat=[]
for i in range(nj):
    a=list(map(int,input().split()))
    mat.append(a)

print(mem(mat))




